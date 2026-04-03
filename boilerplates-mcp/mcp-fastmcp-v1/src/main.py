# Python imports
import os

# Server imports
import uvicorn

# Import the mcp singleton (must happen before services are loaded)
from src.modules import service as mcp_svc

# Import all server tools so they register with the MCP service
import src.server_tools.api_requests_brazil
import src.server_tools.management_markdown

if __name__ == "__main__":

    # Print in the terminal the header of the app
    mcp_svc.show_header()

    # Print in the terminal the folder structure of the container
    mcp_svc.show_folder_structure()

    # Get the underlying HTTP app and apply CORS
    app = mcp_svc.get_app()

    # Start the MCP server using the 
    uvicorn.run(app, host="0.0.0.0", port=8000, ws="wsproto")