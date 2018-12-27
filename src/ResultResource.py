from flask import jsonify
from flask_restful import Resource, Api

# Todo
# shows a single todo item and lets you delete a todo item
from src.models import Result


class ResultResource(Resource):
    def get(self, todo_id):
        '''
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]
        '''
        return 'oi'

    def delete(self, todo_id):
        '''
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204
        '''
        return 'oi'

    def put(self, todo_id):
        return 'oi'
        '''
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
        '''


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class ResultListResource(Resource):
    def get(self):
        return jsonify([i.serialize for i in Result.query.all()])

    def post(self):
        #FixME - implement post method to add new Results
        return 'oi'
        '''
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
        '''
