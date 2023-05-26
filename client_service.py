from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    response = requests.get('http://localhost:5000/todos')
    todos = response.json()
    return jsonify(todos)

@app.route('/todo', methods=['POST'])
def create_todo():
    todo = {'title': 'New Todo', 'completed': False}
    response = requests.post('http://localhost:5000/todos', json=todo)
    created_todo = response.json()
    return jsonify(created_todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    url = f'http://localhost:5000/todos/{todo_id}'
    response = requests.delete(url)
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(port=5001)
