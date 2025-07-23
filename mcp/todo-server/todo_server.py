import json
import datetime
from typing import List, Dict, Any
from pydantic import BaseModel
from fastmcp import FastMCP, Context
import json
import datetime
from typing import List, Dict, Any
from pydantic import BaseModel
from fastmcp import FastMCP, Context

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False
    created_at: str = None

mcp = FastMCP("ToDo Management Server")

todos: List[TodoItem] = [
    TodoItem(id=1, title="Learn FastMCP", completed=False, created_at="2024-01-01"),
    TodoItem(id=2, title="Build sample app", completed=True, created_at="2024-01-02")
]
counter = 3

@mcp.tool()
async def add_todo(title: str, ctx: Context) -> Dict[str, Any]:
    """Add a new ToDo item"""
    global counter

    # Log using the context
    await ctx.info(f"Adding new ToDo: {title}")

    new_todo = TodoItem(
        id=counter,
        title=title,
        created_at=datetime.datetime.now().strftime("%Y-%m-%d")
    )
    todos.append(new_todo)
    counter += 1

    await ctx.info(f"ToDo added: ID {new_todo.id}")

    return {
        "success": True,
        "todo": new_todo.model_dump(),
        "message": f"ToDo '{title}' has been added"
    }

@mcp.resource("todos://all")
def get_all_todos(ctx: Context) -> List[Dict[str, Any]]:
    ctx.info("Fetching all todos")
    return [todo.model_dump() for todo in todos]

if __name__ == "__main__":
    mcp.run()