# Web service imports
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Templates setup
templates = Jinja2Templates(directory="src/templates")

# Instance the fastapi app
app = FastAPI(
    title="docker-uv-htmx",
    version="0.1.0",
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/counter", response_class=HTMLResponse)
async def counter(request: Request, value: int = 0) -> HTMLResponse:
    return templates.TemplateResponse("counter.html", {"request": request, "value": value})

