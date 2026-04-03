# FastMCP Boilerplate

![FastMCP](https://img.shields.io/badge/FastMCP-latest-blue?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.12%2B-yellow?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Supported-blue?style=for-the-badge&logo=docker)
![Podman](https://img.shields.io/badge/Podman-Compatible-purple?style=for-the-badge&logo=podman)

A scalable and secure boilerplate project for rapidly building **Model Context Protocol (MCP)** servers in Python using `fastmcp`. This project is pre-configured with powerful external API tools and a comprehensive suite for securely managing local Markdown repositories safely via the Model Context Protocol.

## 🚀 Key Features

- **FastMCP Built-in:** Built natively on `fastmcp` with `uvicorn` and `wsproto`.
- **Markdown Management Vault:** Fully atomized and async filesystem tools (`aiofiles`, `python-frontmatter`) capable of listing, searching, reading, patching, and writing Markdown files. Implements advanced path validation to avoid directory traversal.
- **API Interfaces:** Extensible integrations ready out-of-the-box (`requests`, `yfinance`, `pyfinance`).
- **Container-Ready:** Ships with a zero-setup `Dockerfile` and `compose.yaml`.

---

## 🛠️ Setup & Configuration

This project is tailored to safely expose local directories as an accessible knowledge vault. To ensure your files map securely inside the container, you must configure your local environment path.

### 1. Configure the Vault Path in `.env`
To power the Markdown Management tools, point the server to a specific folder on your local machine using a `.env` file. 

Create a `.env` file at the root of the project with the following tracking variable:

```env
MARKDOWN_REPO=/absolute/path/to/your/markdown/valut
```

*Note: Replace `/absolute/path/...` with the exact path where your Markdown notes or files live (e.g., `/Users/name/Documents/Vault` or `C:\MyVault`). This makes the boilerplate generic and adaptable across any user's OS and folder structure.*

### 2. How the Security & Directory Syncing Works
In our `compose.yaml`, the `MARKDOWN_REPO` folder is dynamically mounted as a read/write volume mapping explicitly to `/app/markdown_repo` inside the container runtime:

```yaml
volumes:
  - .:/app
  - ${MARKDOWN_REPO}:/app/markdown_repo
```

Every incoming MCP Server request (such as `list_files`, `search_vault`, or `write_markdown`) is rigorously checked by an internal security layer. The server mathematically verifies that the final resolved request strictly scopes within `/app/markdown_repo`. **This prevents malicious actors or the agent from querying arbitrary host details!**

### 3. Permissions on MacOS + Podman Desktop
Container engines (specifically Podman on MacOS) often encounter `Permission Denied` failures when trying to write to host directories. To seamlessly resolve this without altering host folder permissions, the `compose.yaml` explicitly enforces a host user namespace mapping:

```yaml
userns_mode: "keep-id"
```
*This allows the container process to naturally echo your host's exact privileges exclusively for mapped elements, guaranteeing file operations don't fail!*

---

## 💻 Running the Server

Start up the FastMCP instance locally:

```bash
# Using Podman (Recommended for MacOS)
podman-compose up --build

# Using Docker
docker-compose up --build
```
Your MCP server natively attaches and logs folders on startup.

## 📦 Dependencies

Dependencies are managed strictly through Poetry. (See `pyproject.toml`)
- `fastmcp` (Server Layer)
- `python-frontmatter` / `aiofiles` (Markdown parsing & Async file I/O)
- `python-dotenv` (Injecting variables securely)

To build the environment out-of-container:
```bash
poetry install
```
