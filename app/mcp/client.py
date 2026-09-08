

# server_params = StdioServerParameters(
#     command="D:/workspace/aunix-contract/aunixai/agent-connect/.venv/Scripts/python.exe",
#     args=["-m", "app.mcp.server"]
# )

from mcp import Client, StdioServerParameters
from app.mcp.tool_adaptor import build_connector_status_tool


server = StdioServerParameters(
    command="D:/workspace/aunix-contract/aunixai/agent-connect/.venv/Scripts/python.exe",
    args=["-m", "app.mcp.server"]
)


async def connect_to_server():

    async with Client(server) as client:

        tools_result = await client.list_tools()

        mcp_tool = tools_result.tools[0]

        langchain_tool = build_connector_status_tool(
            client,
            mcp_tool
        )

        print(langchain_tool.name)
        print(langchain_tool.description)

        result = await langchain_tool.ainvoke({
             "name": "salesforce"
        })

        print(result)

        # if not tools:
        #     print("no tools found")

        # for tool in tools.tools:
        #     print("Name:", tool.name)
        #     print("Description:", tool.description)
        #     print("Input Schema:", tool.input_schema)
        # result = await client.call_tool("get_connector_status",{
        #      "name": "salesforce"
        # })
        # print("Content:", result.content)
if __name__ == "__main__":
    import asyncio
    asyncio.run(connect_to_server())