# Python standard libs
import multiprocessing, os, sys

# Thir party multi purpose imports
from pyfiglet import Figlet

# Web and services imports
import uvicorn
from fastapi import FastAPI

# Endpoint routers
from endpoints.ping import router as ping_router
from endpoints.game_joke import router as game_joke_router
from endpoints.rand_attrib import router as rand_attrib_router

# Streamlit frontend imports
import streamlit as st
from streamlit.web import cli as stcli

# Create a app object for Uvicorn to start
app = FastAPI()

# Register endpoint routers
app.include_router(ping_router)
app.include_router(game_joke_router)
app.include_router(rand_attrib_router)

# Function to start the FastAPI
def run_fastapi():
    # Points to your app/main.py or where your FastAPI instance is
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=False)

def run_streamlit():
    # Points to the Streamlit entrypoint file.
    # sys.path is fixed there transparently for all pages.
    sys.argv = [
        "streamlit",
        "run",
        "src/streamlit_app.py",
        "--server.port", "8501",
        "--server.address", "0.0.0.0"
    ]

    # Run the streamlit app
    sys.exit(stcli.main())

if __name__ == "__main__":
    # App start headers and decorators
    f = Figlet(font="small")
    print(f.renderText("API boilerplate"))
    print(f.renderText("V 0.1.0"))

    # Create separate processes
    api_process = multiprocessing.Process(target=run_fastapi)
    st_process = multiprocessing.Process(target=run_streamlit)

    # Start processes
    api_process.start()
    st_process.start()

    # Keep the main thread alive
    api_process.join()
    st_process.join()