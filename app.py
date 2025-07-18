from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    todos.append(data)
    return jsonify({"message": "新增成功"}), 201

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if 0 <= index < len(todos):
        deleted = todos.pop(index)
        return jsonify({"message": "刪除成功", "deleted": deleted}), 200
    else:
        return jsonify({"message": "找不到資料"}), 404
