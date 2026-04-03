![Python](https://img.shields.io/badge/python-3.13-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastMCP](https://img.shields.io/badge/FastMCP-005571?style=for-the-badge&logo=mcp)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

---

# 📕 About this boilerplate

This is a pure **MCP (Model Context Protocol)** server boilerplate using **FastMCP**, encapsulated in a Docker container.

## 🛠 Features

- **FastMCP**: Easily create tools, resources, and prompts.
- **Dynamic Registration**: Add new tools/resources/prompts in the `services/` folder, and they are automatically registered.
- **Containerized**: Ready for deployment using Docker or Podman.
- **SSE Support**: Configured to run as an SSE server by default on port 8081.

# 🚀 Quick start guide

1. Build and start the environment:
    ``` zsh
    podman compose up --build
    # or
    docker compose up --build
    ```

2. Access the MCP SSE endpoint:
    * **MCP SSE Server**: `http://localhost:8081/sse`

# 📁 Project structure
```plaintext
app-fastmcp-docker/
├── src/
│   ├── main.py        # Entry point for the container
│   ├── server.py      # FastMCP server instance
│   └── services/      # MCP Components (Auto-registered)
│       ├── __init__.py  # Dynamic discovery logic
│       ├── tools.py     # MCP Tool definitions
│       ├── resources.py # MCP Resource definitions
│       └── prompts.py   # MCP Prompt definitions
├── compose.yaml       # Orchestration & Port mapping
├── Dockerfile         # Python build
├── pyproject.toml     # Dependency management
└── poetry.lock        # Locked dependency tree
```

# 📢 Customizing

To add new functionality:
1. Create a new `.py` file in `src/services/` (or use the existing ones).
2. Use `@mcp.tool()`, `@mcp.resource()`, or `@mcp.prompt()` decorators.
3. The component will be automatically exposed to the MCP server!
