from flask import request

from app import app

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    try:
        todo = TODOS[todo_id]
        resultado = todo
    except KeyError:
        resultado = {'status': 'erro', 'mensagem': f'{todo_id} nao existe!'}
    except Exception:
        resultado = {'status': 'erro', 'mensagem': 'Erro desconhecido!'}
    return resultado


@app.route('/todos2/<todo_id>', methods=['GET', 'PUT', 'DELETE'])
def todos(todo_id):
    if request.method == 'GET':
        resultado = abort_if_todo_doesnt_exist(todo_id)
    elif request.method == 'PUT':
        arg = request.get_json()
        TODOS[todo_id] = {'task': arg['task']}
        resultado = TODOS[todo_id], 201
    elif request.method == 'DELETE':
        if todo_id not in TODOS:
            resultado = abort_if_todo_doesnt_exist(todo_id)
        else:
            del TODOS[todo_id]
            resultado = '', 204
    return resultado


@app.route('/todos2/', methods=['GET', 'POST'])
def todos_list():
    if request.method == 'GET':
        resultado = TODOS
    elif request.method == 'POST':
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = f'todo{todo_id}'
        args = request.get_json()
        TODOS[todo_id] = {'task': args['task']}
        resultado = TODOS[todo_id], 201
    return resultado
