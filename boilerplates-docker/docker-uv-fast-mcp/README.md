# docker-uv-fast-mcp

FastAPI + `uv` boilerplate structured around MCP-style tools.

## How to run

```bash
uv sync
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000
```

Or using Docker / Podman:

```bash
make build
make run
```

Then open:

- `http://localhost:8000/game_one_liners`

