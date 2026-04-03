# docker-uv-htmx

Minimal FastAPI + HTMX boilerplate using `uv`.

## Run with Docker / Podman

```bash
make build
make run
```

Then open:

- `http://localhost:8000/`

## Run locally with uv

```bash
uv sync
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000
```

