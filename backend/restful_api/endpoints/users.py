import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from database.models import User
from restful_api.Exceptions import RoleNotAllowedException
from restful_api.business import create_user, delete_user, update_user

log = logging.getLogger(__name__)

ns = Namespace('users', description='Operations related to users')


user_and_pw = ns.model('User2', {
    'username':fields.String(readOnly=True, description='username'),
    'password': fields.String(readOnly=True, description='password'),
})

user = ns.model('User', {
    'id':fields.Integer(readOnly=True, description='id'),
    'username':fields.String(readOnly=True, description='username'),
    'email': fields.String(readOnly=True, description='email'),
    'role_name': fields.String(readOnly=True, description='role_name'),
    #'uploads': fieds.List(fields.Nested())
})

user_with_password = ns.model('User', {
    'id':fields.Integer(readOnly=True, description='id'),
    'username':fields.String(readOnly=True, description='username'),
    'email': fields.String(readOnly=True, description='email'),
    'role_name': fields.String(readOnly=True, description='role_name'),
    'password': fields.String(readOnly=True, description='password'),
    #'uploads': fieds.List(fields.Nested())
})


@ns.route('/')
class UserCollection(Resource):

    @ns.marshal_list_with(user)
    def get(self):
        """
        Returns list of blog categories.
        """
        users = User.query.all()
        return users

    @ns.response(201, 'Category successfully created.')
    @ns.expect(user_with_password)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        try:
            create_user(data)
        except RoleNotAllowedException as ex:
            return 'Role not recognized. ' \
                   'Exception: {},' \
                   'Errors: {}'.format(ex, ex.errors), 400
        return None, 201


@ns.route('/<int:id>')
@ns.response(404, 'User not found.')
class UserItem(Resource):

    @ns.marshal_with(user)
    def get(self, id):
        """
        Returns a category with a list of posts.
        """
        return User.query.filter(User.id == id).one()

    @ns.expect(user)
    @ns.response(204, 'User successfully updated.')
    def put(self, id):
        """
        Updates a blog category.

        Use this method to change the name of a blog category.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Category Name"
        }
        ```

        * Specify the ID of the category to modify in the request URL path.
        """
        data = request.json
        update_user(id, data)
        return None, 204

    @ns.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes user.
        """
        delete_user(id)
        return None, 204
