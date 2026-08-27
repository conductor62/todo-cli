import sys
print(sys.argv)


import json
import os

FILE = "todo.json"

def load_todos():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

command = sys.argv[1]

if command == "add":
    todos = load_todos()
    new_todo = {
        "id": len(todos) + 1,
        "text": sys.argv[2],
        "done": False
    }
    todos.append(new_todo)
    save_todos(todos)


elif command == "list":
    todos = load_todos()
    for todo in todos:
        status = "✓" if todo["done"] else " "
        print(f"[{status}] {todo['id']}. {todo['text']}")