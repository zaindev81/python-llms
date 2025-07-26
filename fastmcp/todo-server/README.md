# todo-server

## Setup

```sh
uv init

uv venv
source .venv/bin/activate

# install
uv pip install fastmcp pydantic typing asyncio
uv pip install .
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Run

```sh
fastmcp dev todo_server.py
uv run python todo_server.py

# claude
fastmcp install todo_server.py --name "TodoServer"
```

## Test

```sh
uv run python test_client.py

python test_client.py
```

## Claude Desktop

1. Setup Claude MCP configuration in Claude Desktop
2. Restart Claude Desktop

```sh
vim ~/Library/Application\ Support/Claude/claude_desktop_config.json

{
  "mcpServers": {
    "todo-server": {
      "command": "uv",
      "args": ["run", "python", "/path/to/your/todo_server.py"]
    }
  }
}
```
