![Python](https://img.shields.io/badge/python-3.13-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Podman](https://img.shields.io/badge/podman-892CA0?style=for-the-badge&logo=podman&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-%233B2E90.svg?style=for-the-badge&logo=poetry&logoColor=white)

---



# 📕 About this boilerplate

This is a boilerplate for creating FastAPI endpoints encapsulated in a Docker container.

> To find more docker images, visit [Docker Hub](https://hub.docker.com/).
> - Official Python images on docker hub: https://hub.docker.com/_/python
> - This boilerplate uses the [slim bookworm 3.13 python](https://github.com/docker-library/python/blob/d7d46d97a9ffd58269d8d1d0218ce959362b4298/3.13/slim-bookworm/Dockerfile) image.

Developed and teste on:
- macOS:
    - [ x ] 26.2 (Tahoe)
- Linux:
- Windows: 

#### Docker vs Podman

As the developer of this boilerplate I prefer to use Podman over Docker, the files are fully compatible with both.
Some instructions migh look akward if you only use Docker, but they will work and are required for some features of Podman.

> Consider use Podman it's a drop-in replacement for Docker, it's open source, free, lighter and can run rootless.
> - Podman: https://podman.io/


# 🚀 Quick start guide

**Ensure you have docker or podman installed.

1. Clone (or copy the code in) this repository.
2. Build and start the environment:
    ``` zsh
    docker compose up --build
    # or
    podman compose up --build
    ```

If everything wen well, you can see examples of FastAPI endpoints, and simple streamlit frontend:
* API (FastAPI) (PRD): http://localhost:8000
* API (FastAPI) (DEV): http://localhost:8080
* Frontend (Streamlit): http://localhost:8501


# 📁 Project main structure
```` Plaintext
app-fastapi-docker/
├── app/
│   ├── __init__.py    # Package initializer
│   ├── main.py        # Entry point (FastAPI + Uvicorn)
│   ├── endpoints/     # FastAPI route handlers
│   ├── logs/          # General logs of the app
│   ├── modules/       # Shared business logic & utils
│   └── pages/         # Streamlit multipage files
├── compose.yaml       # Orchestration & Port mapping
├── Dockerfile         # Python 3.13 slim-bookworm build
├── pyproject.toml     # Dependency management
└── poetry.lock        # Locked dependency tree
````

# 📢 Making it your own

To develop on top of this boilerplate, dont forget to:
* This app uses [poetry](https://python-poetry.org/) for dependency management, every new python lib you add, must be added to the project via poetry, use `poetry add <package-name>`.
* We're using a lightweight docker image, it may not contain all the linux/unix tools you expect, maybe you need to change the default docker image.
* Be aware of the name of the app, it's a general **Korza** app, you must change it for professional deploy and usage.
* To run this service, we use `uvicorn`, it's a production-ready ASGI server for FastAPI, and bind the execution of all services to `0.0.0.0` inside the container.

# Cool links for customizations
* Google material icons set: https://fonts.google.com/icons
* Emoji picker: https://nolanlawson.github.io/emoji-picker-element/


