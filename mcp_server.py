from mcp.server.fastmcp import FastMCP

# Open port 8000
mcp = FastMCP(name="mcp-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def get_current_temperature(city_name: str) -> str:
    """Get the current temperature in a city."""
    return f"Current temperature in {city_name} is 25°C."

@mcp.resource("resource://ma_so_thue")
def get_ma_so_thue() -> str:
    """Get tax code."""
    return "123456789"

@mcp.resource("resource://say_hi/{name}")
def say_hi(name: str) -> str:
    """Say hi to people with name."""
    return f"Hi {name}!"

@mcp.prompt()
def review_sentence(sentence: str) -> str:
    return "Review this sentence, remove any personal information: \n\n{}".format(sentence)

if __name__ == "__main__":
    # print("Starting MCP server...")
    # Run the server with SSE transport
    mcp.run(transport='stdio') # stdio

