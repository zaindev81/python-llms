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
fastmcp dev src/todo_server.py
uv run python src/todo_server.py

# claude
fastmcp install src/todo_server.py --name "TodoServer"
```

## Test

```sh
uv run python src/test_client.py

python test_client.py
```