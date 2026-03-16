# ==========================================
# personal-boilerplates-fast-api
# ==========================================

# Auto-detect docker or podman
COMPOSE := $(shell which docker > /dev/null 2>&1 && echo "docker compose" || echo "podman compose")

# ==========================================

.PHONY: help build up dev down logs shell restart clean rebuild test test-spec

# Default target — shows help
help:
	@echo ""
	@echo "  Using: $(COMPOSE)"
	@echo ""
	@echo "  build           Build the image"
	@echo "  run             Start the container"
	@echo "  build-up        Start with build"
	@echo "  build-run       Start with build"
	@echo ""

# Build the image
build:
	$(COMPOSE) build

# Start container
up:
	$(COMPOSE) up

# Do the same as up, just a alias
run:
	$(COMPOSE) up

# Start the container and build the image (the same as build + run)
build-up:
	$(COMPOSE) up --build

# Start the container and build the image (the same as build + run)
build-run:
	$(COMPOSE) up --build
