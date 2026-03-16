# Using slim debian stable image (Docker + Podman compatible)
FROM docker.io/library/python:3.13-slim-bookworm

# Docker labeling
LABEL personal.boilerplates.name="docker-uv-fast-api" \
      personal.boilerplates.version="1.0.0" \
      personal.boilerplates.created="2026-03-16" \
      personal.boilerplates.authors="marcelo.bracali"

# Install uv on the machine
RUN apt-get update && apt-get install -y curl ca-certificates \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && rm -rf /var/lib/apt/lists/*

# Configure uv environment
ENV PATH="/root/.local/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    UV_PROJECT_ENVIRONMENT=/app/.venv

# Use app as the workdir
WORKDIR /app

# Copy project metadata first (for dependency caching)
COPY pyproject.toml uv.lock ./

# Sync uv dependencies (before copying source for cache efficiency)
RUN uv sync --frozen --no-dev

# Copy the rest of the application to the container
COPY . .

# As a best practice add a user to run the app (non-root)
RUN useradd -m boilerplater && chown -R boilerplater /app
USER boilerplater

# API port
EXPOSE 8000

# Runs the app through the uv environment
CMD ["uv", "run", "python", "-m", "src.main"]