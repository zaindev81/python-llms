# server

```sh
uv init

uv venv
source .venv/bin/activate

uv pip install fastmcp
```

## Run

```sh
fastmcp dev simple_server.py
uv run python simple_server.py

fastmcp install simple_server.py --name "SimpleServer"
```

## Test

```sh
python test_client.py

uv run python simple_server.py
uv run python test_client.py
```