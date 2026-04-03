.PHONY: build run test podman-build podman-run podman-test

# ── Docker ────────────────────────────────────────────────────────────────────

build:
	docker compose build

run:
	docker compose up

build-run:
	docker compose up --build

# ── Podman ────────────────────────────────────────────────────────────────────

podman-build:
	podman compose build

podman-run:
	podman compose up

podman-build-run:
	podman compose up --build
