# fastmcp-poc

Learning FastMCP

It is recommended to use uv.

```shell
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate

# Creates venv and installs dependencies
uv sync 
```

Once uv installs fastmcp package, we can verify it like:

```shell
fastmcp version

# you should see something like below
FastMCP version:                                                     2.14.1
MCP version:                                                         1.25.0
Python version:                                                      3.12.9
Platform:                                        macOS-26.1-arm64-arm-64bit
FastMCP                     /Users/.../fastmcp-poc/.venv/lib/python3.14/...
```

Or, we can use fastmcp cli to run the server:

```shell
# stdio
fastmcp run server.py:mcp

# or HTTP transport
fastmcp run server.py:mcp --transport http --port 8000
```