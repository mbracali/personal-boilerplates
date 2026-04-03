# Web service imports
from fastapi import FastAPI

# Import endpoints
from src.endpoints.game_one_liners import router as game_joke_router

# Instance the fastapi app
app = FastAPI(
    title="personal-boilerplates",
    version="1.0.0",
)

# Register endpoints
app.include_router(game_joke_router)