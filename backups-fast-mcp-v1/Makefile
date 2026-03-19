.PHONY: build run test podman-build podman-run podman-test

# ── Docker ────────────────────────────────────────────────────────────────────

build:
	docker compose build

run:
	docker compose up

build-run:
	docker compose up --build

# docker compose run --rm app poetry run python -m pytest tests/ -v -s
test: build
	docker compose run --rm app poetry run python -m pytest tests/ -v

# ── Podman ────────────────────────────────────────────────────────────────────

podman-build:
	podman compose build

podman-run:
	podman compose up

podman-build-run:
	podman compose up --build

# podman compose run --rm app poetry run python -m pytest tests/ -v -s
podman-test: podman-build
	podman compose run --rm app poetry run python -m pytest tests/ -v -s

# Only Brazil tests
podman-test-spec-brazil: podman-build
	podman compose run --rm app poetry run python -m pytest tests/test_brazilian_expert.py -v -s

# Only Finance tests
podman-test-spec-finances: podman-build
	podman compose run --rm app poetry run python -m pytest tests/test_finances_expert.py -v -s
