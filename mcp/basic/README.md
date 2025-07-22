# basic

```sh
uv venv
uv sync --extra dev

cp .env.example .env

uv pip install fastmcp
```

```sh
uv run server.py
uv run pytest --cov=src --cov=examples --cov-report=html
```
