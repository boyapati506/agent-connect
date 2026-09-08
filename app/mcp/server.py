from mcp.server import MCPServer

mcp = MCPServer("AgentConnect")


@mcp.tool()
def get_connector_status(name: str) -> dict:
    """Get the status of an AgentConnect connector by name."""

    return {
        "name": name,
        "status": "ACTIVE"
    }


if __name__ == "__main__":
    mcp.run()