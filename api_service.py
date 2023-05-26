from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def get_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.json
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(port=5000)
