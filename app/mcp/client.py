from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="D:\workspace\aunix-contract\aunixai\agent-connect\.venv\Scripts\python.exe",
    args=["-m", "app.mcp.server"]
)

async def connect_to_server():
    async with stdio_client(server_params) as (read,write):
        print("connected to mcp server")

        async with ClientSession(read,write) as session:
            await session.initialize()
            print("session initialized")