from app import api
from app.learning_with.modelTodo import Todo, TodoList

api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos/')
