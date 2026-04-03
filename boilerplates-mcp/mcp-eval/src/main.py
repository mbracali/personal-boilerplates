# Python imports
import os

# Server imports
import uvicorn
from starlette.middleware.cors import CORSMiddleware

# External imports
from pyfiglet import Figlet

# Import the mcp singleton (must happen before services are loaded)
from src.mcp_instance import mcp

# Import services package to trigger dynamic registration of tools, resources, and prompts
from src import services

if __name__ == "__main__":
    # App start headers
    f = Figlet(font="small")
    print(f.renderText("FastMCP Boilerplate"))
    print(f.renderText("V 0.1.0"))

    # Print all folders in the container at startup (2 levels deep)
    print("📁 Container folders at /app:")
    for item in sorted(os.listdir("/app")):
        full = os.path.join("/app", item)
        kind = "📂" if os.path.isdir(full) else "📄"
        print(f"  {kind} {item}")
        if os.path.isdir(full):
            for sub in sorted(os.listdir(full)):
                sub_full = os.path.join(full, sub)
                sub_kind = "📂" if os.path.isdir(sub_full) else "📄"
                print(f"    {sub_kind} {sub}")

    # Get the underlying HTTP app and apply CORS
    app = mcp.http_app()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Start the MCP server using the customized app instance
    # Use wsproto as the WebSocket backend to avoid websockets.legacy deprecation warnings
    uvicorn.run(app, host="0.0.0.0", port=8081, ws="wsproto")