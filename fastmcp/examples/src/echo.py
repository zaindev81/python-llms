from fastmcp import FastMCP

mcp = FastMCP("Echo Server")

@mcp.tool
def echo_tool(text: str) -> str:
    """Echo the input text"""
    return text

@mcp.resource("echo://static")
def echo_resource() -> str:
    return "Echo!"

@mcp.resource("echo://{text}")
def echo_template(text: str) -> str:
    """Echo the input text with a template"""
    return f"Echo: {text}"

@mcp.prompt("echo")
def echo_prompt(text: str) -> str:
    """Echo the input text via prompt"""
    return text

if __name__ == "__main__":
    mcp.run()