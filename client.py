import asyncio
from fastmcp import Client

async def main():
  """Connect to MCP server and call tools"""
  client = Client("http://localhost:8000/mcp")
  
  async with client:
    # List available tools
    tools = await client.list_tools()
    print("Available tools:")
    for tool in tools:
      print(f"  - {tool.name}: {tool.description}")
    print()
    
    # Test add
    result = await client.call_tool("add", {"a": 10, "b": 20})
    print(f"add(10, 20) = {result}")
    
    # Test subtract
    result = await client.call_tool("subtract", {"a": 50, "b": 15})
    print(f"subtract(50, 15) = {result}")
    
    # Test multiply
    result = await client.call_tool("multiply", {"a": 7, "b": 8})
    print(f"multiply(7, 8) = {result}")
    
    # Test divide
    result = await client.call_tool("divide", {"a": 100.0, "b": 4.0})
    print(f"divide(100, 4) = {result}")
    
    # Test power
    result = await client.call_tool("power", {"base": 2, "exponent": 10})
    print(f"power(2, 10) = {result}")
    
    # Test modulo
    result = await client.call_tool("modulo", {"a": 17, "b": 5})
    print(f"modulo(17, 5) = {result}")

if __name__ == "__main__":
  asyncio.run(main())

