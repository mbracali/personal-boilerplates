import os
import re
import aiofiles
import frontmatter
from typing import List, Dict, Any, Optional

# Import the custom mcp service layer
from src.modules import service as mcp_svc

# Get the configured MCP singleton object
mcp = mcp_svc.mcp

class MarkdownManager:
    """
    Handles secure, atomic, and asynchronous Markdown file operations
    for the MCP server.
    """
    def __init__(self):
        # In Docker/Podman, the external repository is mounted to /app/markdown_repo 
        # (check compose.yaml volumes). We cannot read the .env MARKDOWN_REPO inside the container
        # because that variable holds the macOS host path (/Users/bracali/...), which the container
        # has zero permission to traverse internally.
        
        self.base_dir = os.path.abspath("/app/markdown_repo")
        
        # Ensure the base directory exists
        if not os.path.exists(self.base_dir):
            try:
                os.makedirs(self.base_dir, exist_ok=True)
            except PermissionError:
                pass # If it's a read-only bind mount, ignore instead of crashing

    def validate_safe_path(self, requested_path: str) -> str:
        """
        Validates the requested path to prevent directory traversal attacks (Chroot logic).
        """
        # Strip leading slashes to prevent absolute path hijacking
        clean_path = requested_path.lstrip("/")
        
        # Resolve the full absolute path
        full_path = os.path.abspath(os.path.join(self.base_dir, clean_path))
        
        # Ensure the resolved path strictly starts with the base directory
        if not full_path.startswith(self.base_dir):
            raise PermissionError(f"Path '{requested_path}' escapes the allowed BASE_DIR.")
            
        return full_path

manager = MarkdownManager()

# --- TOOL 1: list_files ---
@mcp.tool(annotations={"title": "List all Markdown files in a directory"})
async def list_files(path: str = ".") -> Any:
    """
    Recursively scans the directory for .md and .markdown files.
    Returns a list of dictionaries with relative paths and file sizes.
    """
    try:
        target_dir = manager.validate_safe_path(path)
        
        if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
            return {"error": f"Error: Directory '{path}' does not exist or is not a directory."}

        results = []
        # Walk through directory
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith((".md", ".markdown")):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, manager.base_dir)
                    size = os.path.getsize(full_path)
                    results.append({"path": rel_path, "size_bytes": size})
                    
        return {"files": results}
        
    except PermissionError:
        return {"error": f"Error: OS level permission denied at '{path}'."}
    except Exception as e:
        return {"error": f"Error accessing directory: {str(e)}"}


# --- TOOL 2: read_markdown ---
@mcp.tool(annotations={"title": "Read a Markdown file and parse metadata"})
async def read_markdown(path: str) -> Any:
    """
    Reads a Markdown file and separates YAML metadata from raw content.
    """
    try:
        full_path = manager.validate_safe_path(path)
        
        if not os.path.exists(full_path):
            return {"error": f"Error: File '{path}' does not exist. Use list_files to verify."}

        async with aiofiles.open(full_path, mode='r', encoding='utf-8') as f:
            raw_content = await f.read()

        # Parse frontmatter
        try:
            parsed = frontmatter.loads(raw_content)
            return {
                "metadata": parsed.metadata,
                "content": parsed.content
            }
        except Exception:
            return {"error": "Error: Invalid YAML frontmatter structure detected."}

    except PermissionError:
        return {"error": f"Error: OS level permission denied at '{path}'."}
    except Exception as e:
        return {"error": f"Error reading file: {str(e)}"}


# --- TOOL 3: write_markdown ---
@mcp.tool(annotations={"title": "Atomically write a Markdown file with metadata"})
async def write_markdown(path: str, content: str, metadata: dict = None) -> Any:
    """
    Atomically writes a Markdown file, injecting YAML frontmatter if metadata is provided.
    """
    try:
        full_path = manager.validate_safe_path(path)
        
        # Ensure parent directories exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Prepare the file content
        if metadata is not None:
            post = frontmatter.Post(content, **metadata)
            final_content = frontmatter.dumps(post)
        else:
            final_content = content

        # Atomic move strategy: write to .tmp, then replace
        tmp_path = full_path + ".tmp"
        
        async with aiofiles.open(tmp_path, mode='w', encoding='utf-8') as f:
            await f.write(final_content)
            
        # Atomic rename (POSIX os.replace/rename is atomic)
        os.replace(tmp_path, full_path)
        
        return {"success": True, "message": f"Successfully wrote {path}"}
        
    except PermissionError:
        return {"error": f"Error: OS level permission denied at '{path}'."}
    except Exception as e:
        # Clean up tmp file if rename failed
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)
        return {"error": f"Error writing file: {str(e)}"}


# --- TOOL 4: patch_section ---
@mcp.tool(annotations={"title": "Patch a specific section in a Markdown file"})
async def patch_section(path: str, heading: str, new_content: str) -> Any:
    """
    Replaces a specific section of a Markdown file identified by a heading.
    """
    try:
        full_path = manager.validate_safe_path(path)
        
        if not os.path.exists(full_path):
            return {"error": f"Error: File '{path}' does not exist. Use list_files to verify."}

        async with aiofiles.open(full_path, mode='r', encoding='utf-8') as f:
            raw_content = await f.read()

        # Parse frontmatter to preserve metadata
        try:
            parsed = frontmatter.loads(raw_content)
        except Exception:
            return {"error": "Error: Invalid YAML frontmatter structure detected."}

        # Parse the content line by line to find the section
        lines = parsed.content.split('\n')
        
        # Find the target heading
        heading_level = 0
        start_idx = -1
        
        for i, line in enumerate(lines):
            # Clean heading match (e.g. "## My Heading")
            match = re.match(r'^(#{1,6})\s+(.*)', line)
            if match and match.group(2).strip() == heading.strip():
                heading_level = len(match.group(1))
                start_idx = i
                break
                
        if start_idx == -1:
            return {"error": f"Error: Heading '{heading}' not found in file."}
            
        # Find the end of the section (next heading of same or higher level)
        end_idx = len(lines)
        for i in range(start_idx + 1, len(lines)):
            match = re.match(r'^(#{1,6})\s+', lines[i])
            if match:
                current_level = len(match.group(1))
                if current_level <= heading_level:
                    end_idx = i
                    break
                    
        # Replace the section
        new_section_lines = [lines[start_idx]] + new_content.split('\n')
        if new_section_lines[-1] != "":
            new_section_lines.append("") # trailing newline
            
        modified_lines = lines[:start_idx] + new_section_lines + lines[end_idx:]
        modified_content = '\n'.join(modified_lines)
        
        # Use the atomic write logic
        post = frontmatter.Post(modified_content, **parsed.metadata)
        final_content = frontmatter.dumps(post)
        
        tmp_path = full_path + ".tmp"
        async with aiofiles.open(tmp_path, mode='w', encoding='utf-8') as f:
            await f.write(final_content)
        os.replace(tmp_path, full_path)

        return {"success": True, "message": f"Successfully patched section '{heading}' in {path}"}

    except PermissionError:
        return {"error": f"Error: OS level permission denied at '{path}'."}
    except Exception as e:
        return {"error": f"Error patching file: {str(e)}"}


# --- TOOL 5: search_vault ---
@mcp.tool(annotations={"title": "Search vault for query using generator"})
async def search_vault(query: str, use_regex: bool = False) -> Any:
    """
    Searches all Markdown files in the vault for a query (exact or regex).
    Streams lines to minimize memory usage for large vaults.
    """
    try:
        if use_regex:
            pattern = re.compile(query)
            
        matches = []
        
        # We need an async generator wrapper to do async file I/O safely
        async def scan_files():
            for root, _, files in os.walk(manager.base_dir):
                for file in files:
                    if file.endswith((".md", ".markdown")):
                        yield os.path.join(root, file)

        async for full_path in scan_files():
            try:
                rel_path = os.path.relpath(full_path, manager.base_dir)
                line_idx = 1
                
                async with aiofiles.open(full_path, mode='r', encoding='utf-8') as f:
                    async for line in f:
                        found = False
                        if use_regex:
                            if pattern.search(line):
                                found = True
                        else:
                            if query in line:
                                found = True
                                
                        if found:
                            matches.append({
                                "file": rel_path,
                                "line_number": line_idx,
                                "match": line.strip()[:200] # Limit context snippet size
                            })
                            
                            # Limit total search results to protect token usage constraints
                            if len(matches) >= 50:
                                matches.append({"warning": "Search hit 50 result limit. Refine query."})
                                return {"results": matches}
                                
                        line_idx += 1
                        
            except Exception:
                # If a single file fails to read uniquely, skip it (e.g. bad encoding)
                continue
                
        return {"results": matches}
        
    except Exception as e:
        return {"error": f"Error during vault search: {str(e)}"}
