from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

# 載入 todos 資料
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        todos = json.load(f)
else:
    todos = []

# 計算下一個 id
next_id = max([todo["id"] for todo in todos], default=0) + 1

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    global next_id
    data = request.json
    new_todo = {"id": next_id, "title": data["title"]}
    todos.append(new_todo)
    next_id += 1
    save_todos()
    return jsonify(new_todo), 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            save_todos()
            return jsonify({"message": "刪除成功"}), 200
    return jsonify({"message": "找不到資料"}), 404

def save_todos():
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f)

if __name__ == "__main__":
    app.run(debug=True)
