from fastmcp import FastMCP

mcp = FastMCP("Demo MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
  """Add two numbers"""
  return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
  """Subtract b from a"""
  return a - b

@mcp.tool
def multiply(a: int, b: int) -> int:
  """Multiply two numbers"""
  return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
  """Divide a by b"""
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

@mcp.tool
def power(base: int, exponent: int) -> int:
  """Raise base to the power of exponent"""
  return base ** exponent

@mcp.tool
def modulo(a: int, b: int) -> int:
  """Get remainder of a divided by b"""
  if b == 0:
    raise ValueError("Cannot modulo by zero")
  return a % b

if __name__ == "__main__":
  # run with stdio - traditional way to connect MCP servers to clients
  # mcp.run()

  # run with http - enables remote connections
  mcp.run(transport="http", port=8000)

