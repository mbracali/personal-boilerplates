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

# Copy poetry.lock and pyproject.toml to the container and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Copy the rest of the application to the container
COPY . .

# As a best practice add a user to run the app (non-root)
RUN useradd -m korza_runner && chown -R korza_runner /app
USER korza_runner

# API / Backend (FastAPI, Flask, etc.)
EXPOSE 8000

# Proxy / Alternative API
EXPOSE 8080

# Frontend (Streamlit-friendly)
EXPOSE 8501

# Smaller buffer size to force print logs immediately
ENV PYTHONUNBUFFERED=1
# Turn it off if your app prints too much info on the terminal
ENV PYTHONPATH=/app/src


# Runs the app through the poetry environment
CMD ["poetry", "run", "python", "-m", "src.main"]

