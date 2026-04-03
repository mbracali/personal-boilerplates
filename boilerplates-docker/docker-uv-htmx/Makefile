# ==========================================
# docker-uv-htmx
# ==========================================

# Auto-detect docker or podman
COMPOSE := $(shell which docker > /dev/null 2>&1 && echo "docker compose" || echo "podman compose")

# ==========================================

.PHONY: help build up run build-up build-run

help:
	@echo ""
	@echo "  Using: $(COMPOSE)"
	@echo ""
	@echo "  build           Build the image"
	@echo "  run             Start the container"
	@echo "  build-up        Start with build"
	@echo "  build-run       Start with build"
	@echo ""

build:
	$(COMPOSE) build --no-cache

up:
	$(COMPOSE) up

run:
	$(COMPOSE) up

build-up:
	$(COMPOSE) down --remove-orphans
	$(COMPOSE) up --build --no-cache

build-run:
	$(COMPOSE) down --remove-orphans
	$(COMPOSE) up --build --no-cache

