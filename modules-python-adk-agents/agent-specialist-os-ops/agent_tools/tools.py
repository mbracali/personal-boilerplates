import os
import glob
from pathlib import Path

# --- CONSTANTS ---
ALLOWED_EXTENSIONS = {'.md', '.json', '.yaml', '.toml', '.txt'}
# We define the output directory relative to the current working directory
OUTPUT_DIR = os.path.abspath(os.path.join(os.getcwd(), "agent_artifacts"))

# --- FILE WRITING OPERATIONS ---
def write_output_file(filename: str, content: str) -> dict:
    """
    Writes content to a file inside the './agent_artifacts' folder.
    Only allows formats: .md, .json, .yaml, .toml, and .txt.
    
    Args:
        filename (str): The name of the file to be created (e.g., 'data.json'). Must include extension.
        content (str): The text content to write into the file.
    """
    try:
        # Check an allowed extension
        _, ext = os.path.splitext(filename)
        if ext.lower() not in ALLOWED_EXTENSIONS:
            return {"error": f"Format '{ext}' is not allowed. Allowed formats are: {', '.join(ALLOWED_EXTENSIONS)}"}

        # Ensure the output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Prevent directory traversal attacks
        safe_filename = os.path.basename(filename)
        file_path = os.path.join(OUTPUT_DIR, safe_filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return {
            "status": "success",
            "message": f"File '{safe_filename}' written successfully.",
            "path": file_path
        }
    except Exception as e:
        return {"error": f"Failed to write file: {str(e)}"}

# --- FILE SEARCH AND VISUALIZATION OPERATIONS ---
def list_directory(directory_path: str = ".") -> dict:
    """
    Lists all files and subdirectories within a given directory path.
    Useful for an agent to understand the structure of the project.
    
    Args:
        directory_path (str): The path to the directory to list (defaults to current dir '.').
    """
    try:
        resolved_path = os.path.abspath(directory_path)
        if not os.path.exists(resolved_path):
            return {"error": f"Directory not found: {resolved_path}"}
        if not os.path.isdir(resolved_path):
            return {"error": f"Path is not a directory: {resolved_path}"}

        items = os.listdir(resolved_path)
        files = []
        directories = []
        
        for item in items:
            item_path = os.path.join(resolved_path, item)
            if os.path.isdir(item_path):
                directories.append(item)
            else:
                files.append(item)

        return {
            "current_directory": resolved_path,
            "directories": sorted(directories),
            "files": sorted(files)
        }
    except Exception as e:
        return {"error": f"Failed to list directory: {str(e)}"}


def read_file_content(filepath: str) -> dict:
    """
    Reads and visualizes the contents of a specific file inside the container.
    
    Args:
        filepath (str): The full or relative path to the file to be read.
    """
    try:
        resolved_path = os.path.abspath(filepath)
        if not os.path.exists(resolved_path):
            return {"error": f"File not found: {resolved_path}"}
        if not os.path.isfile(resolved_path):
            return {"error": f"Path is not a file: {resolved_path}"}

        with open(resolved_path, "r", encoding="utf-8") as f:
            content = f.read()

        return {
            "status": "success",
            "file": resolved_path,
            "content": content
        }
    except UnicodeDecodeError:
        return {"error": "Failed to read file. It might be a binary file."}
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}


def search_files_by_pattern(directory_path: str, pattern: str) -> dict:
    """
    Recursively searches for files matching a specific pattern within a directory.
    
    Args:
        directory_path (str): The path to start the search from (e.g., '.').
        pattern (str): The glob pattern to search for (e.g., '*.py' or '**/*.md').
    """
    try:
        resolved_path = os.path.abspath(directory_path)
        if not os.path.exists(resolved_path):
            return {"error": f"Directory not found: {resolved_path}"}

        search_path = os.path.join(resolved_path, "**", pattern)
        matches = glob.glob(search_path, recursive=True)
        
        return {
            "status": "success",
            "search_directory": resolved_path,
            "pattern": pattern,
            "matches_found": len(matches),
            "files": sorted(matches)
        }
    except Exception as e:
        return {"error": f"Failed to search files: {str(e)}"}
