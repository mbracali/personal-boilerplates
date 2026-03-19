# Created in 2026-02-14

# Using slim debian stable image (Docker + Podman compatible)
FROM docker.io/library/python:3.13-slim-bookworm

# Configuring poetry behavior
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1

# Use app as the workdir
WORKDIR /app

# Install poetry on the machine
RUN pip install --no-cache-dir poetry

# Copy the application source to the container
COPY boilerplate-fast-mcp/ .
RUN poetry install --no-root

# MCP Server (SSE)
EXPOSE 8000

# Smaller buffer size to force print logs immediately
ENV PYTHONUNBUFFERED=1
# Turn it off if your app prints too much info on the terminal
ENV PYTHONPATH=/app

# Runs the app through the poetry environment
CMD ["poetry", "run", "python", "-m", "src.main"]
