from langchain_core.tools import StructuredTool


def build_connector_status_tool(client, mcp_tool):

    async def invoke_mcp_tool(name: str):
        result = await client.call_tool(
            mcp_tool.name,
            {
                "name": name
            }
        )

        if result.structured_content is not None:
            return result.structured_content

        return result.content

    return StructuredTool.from_function(
        coroutine=invoke_mcp_tool,
        name=mcp_tool.name,
        description=mcp_tool.description or ""
    )