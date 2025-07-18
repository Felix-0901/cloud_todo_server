from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []
next_id = 1  # 每筆 todo 的唯一 ID


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    global next_id
    data = request.json
    title = data.get("title")
    if not title:
        return jsonify({"message": "標題不可為空"}), 400

    new_todo = {"id": next_id, "title": title}
    todos.append(new_todo)
    next_id += 1
    return jsonify(new_todo), 201


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return jsonify({"message": "刪除成功", "deleted": todo}), 200
    return jsonify({"message": "找不到這筆 todo"}), 404


if __name__ == "__main__":
    app.run(debug=True)
