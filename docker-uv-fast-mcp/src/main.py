# Web service imports
from fastapi import FastAPI

# Import tools
from src.tools.game_one_liners import router as game_one_liners_router

# Instance the fastapi app
app = FastAPI(
    title="personal-boilerplates-mcp",
    version="1.0.0",
)

# Register tools
app.include_router(game_one_liners_router)

