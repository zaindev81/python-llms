# examples

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install fastmcp
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Development

```sh
# basic
uv run python src/basic.py
uv run python src/test_basic.py

# echo
uv run python src/echo.py
uv run python src/test_echo.py

# config
uv run src/config_server.py
uv run src/config_server.py --name MyServer --debug
```