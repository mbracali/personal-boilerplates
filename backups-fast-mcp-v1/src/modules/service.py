"""
This file contains some loose methods that are used in various parts
of the application.
"""

# Default python imports
import os

# External imports
from pyfiglet import Figlet

# Service related imports
from fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware

# Load the mcp behavior file to feed into the MCP server
with open("./src/server_docs/mcp_behavior.md", "r", encoding="utf-8") as f:
    instructions_string = f.read()

# Create the mcp object ONCE — imported by main.py and all services
mcp = FastMCP(name="MCP-Boilerplate", instructions=instructions_string)

def show_header():
    """
    Print the header of the app
    """
    
    # Render the name of the app with the pyfiglet
    f = Figlet(font="small")
    print(f.renderText("FastMCP"))
    print(f.renderText("V 0.1.0"))

def show_folder_structure():
    """
    Print the folder structure of the container
    """
    
    # Print all folders in the container at startup (2 levels deep)
    print("📁 Container folders at /app:")
    for item in sorted(os.listdir("/app")):
        full = os.path.join("/app", item)
        kind = "📂" if os.path.isdir(full) else "📄"
        print(f"  {kind} {item}")
        if os.path.isdir(full):
            try:
                sub_items = sorted(os.listdir(full))
                for sub in sub_items:
                    sub_full = os.path.join(full, sub)
                    sub_kind = "📂" if os.path.isdir(sub_full) else "📄"
                    print(f"    {sub_kind} {sub}")
                    
                    # If this sub-folder is our mounted external repository, show 1 more level deep!
                    if item == "markdown_repo" or sub == "markdown_repo":
                        if os.path.isdir(sub_full):
                            try:
                                nested_items = sorted(os.listdir(sub_full))
                                # Only show up to 10 items to prevent enormous logs if the vault is huge
                                for nested in nested_items[:10]:
                                    nested_full = os.path.join(sub_full, nested)
                                    nested_kind = "📂" if os.path.isdir(nested_full) else "📄"
                                    print(f"      {nested_kind} {nested}")
                                if len(nested_items) > 10:
                                    print(f"      ... and {len(nested_items) - 10} more items")
                            except PermissionError:
                                print("      🔒 Permission Denied")
            except PermissionError:
                print("    🔒 Permission Denied")
    print("")


def get_app():
    """
    Return a fastmcp object
    """

    # Get the underlying HTTP app from the MCP object
    app = mcp.http_app()
    
    # Apply CORS rules
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Return the app object
    return app









