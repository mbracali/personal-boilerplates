FROM docker.io/library/python:3.14-slim-bookworm

# Docker labeling
LABEL personal.boilerplates.name="docker-uv-fast-mcp" \
      personal.boilerplates.version="0.1.0" \
      personal.boilerplates.created="2026-03-16" \
      personal.boilerplates.authors="marcelo.bracali"

# Install uv on the machine
RUN apt-get update && apt-get install -y curl ca-certificates \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && cp /root/.local/bin/uv /usr/local/bin/uv \
    && chmod +x /usr/local/bin/uv \
    && rm -rf /var/lib/apt/lists/*

# Create app dir before we work there
RUN mkdir -p /app

# Configure environment
ENV PATH="/usr/local/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    UV_PROJECT_ENVIRONMENT=/app/.venv

# Work as root while building deps
WORKDIR /app

# Copy project metadata first (for dependency caching)
COPY pyproject.toml uv.lock ./

# Sync uv dependencies (creates /app/.venv)
RUN uv sync --frozen --no-dev

# Now create non-root user and give it ownership of /app and the venv
RUN useradd -m boilerplater \
    && chown -R boilerplater:boilerplater /app

USER boilerplater

# Copy the rest of the application to the container
COPY . .

# API port
EXPOSE 8000

# Run the FastAPI app via uvicorn through uv
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

