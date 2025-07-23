import asyncio
import json
from fastmcp import Client

async def test_server():
    try:
        async with Client("todo_server.py") as client:
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")
            print()

            resources = await client.list_resources()
            for resource in resources:
                print(f"  - {resource.uri}: {resource.description}")
            print()

            print("1. Initial ToDo list:")
            todos = await client.read_resource("todos://all")
            initial_todos = json.loads(todos[0].text)
            for todo in initial_todos:
                status = "✅" if todo["completed"] else "⏳"
                print(f"  {status} [{todo['id']}] {todo['title']}")
            print()

            print("2. Summary of ToDos:")
            summary = await client.read_resource("todos://summary")
            summary_data = json.loads(summary[0].text)
            print(f"Total: {summary_data['total']}, Completed: {summary_data['completed']}, Pending: {summary_data['pending']}, Completion Rate: {summary_data['completion_rate']}%")

            print("3. Adding a new ToDo:")
            result = await client.call_tool("add_todo", {
                "title": "Read the FastMCP documentation"
            })
            add_result = json.loads(result.content[0].text)
            print(f"  ✅ {add_result['message']}")
            print()

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_server())