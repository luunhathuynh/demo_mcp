from mcp import ClientSession
from mcp.client.sse import sse_client

async def test_sse_client():
    async with sse_client("http://0.0.0.0:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Call add tool
            result = await session.call_tool("add", arguments={"a": 4, "b": 6})
            print("Result of add tool:", result)

            # Get tax code
            result = await session.read_resource("resource://ma_so_thue")
            print("Tax code:", result)

            # Say hi
            result = await session.read_resource("resource://say_hi/LuuDepTrai")
            print("Say hi:", result)

            # Prompt
            prompt = await session.get_prompt("review_sentence", arguments={"sentence": "So chung minh nhan dan la 987654321"})
            print("Prompt:", prompt)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_sse_client())