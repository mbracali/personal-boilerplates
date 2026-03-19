from fastmcp import FastMCP

# Load the instructions
with open("./src/instruction.md", "r", encoding="utf-8") as f:
    instructions_string = f.read()

# Create the mcp object — imported by main.py and all services
mcp = FastMCP(name="MCP-Boilerplate", instructions=instructions_string)
