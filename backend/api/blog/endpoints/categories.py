import logging

from flask import request
from flask_restplus import Resource

from api.Exceptions import RoleNotAllowedException
from api.blog.business import create_user, delete_user, update_user
from api.blog.serializers import category, user, user_with_password
from api.restplus import api
from database.models import User

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to users')


@ns.route('/')
class UserCollection(Resource):

    @api.marshal_list_with(user)
    def get(self):
        """
        Returns list of blog categories.
        """
        users = User.query.all()
        return users

    @api.response(201, 'Category successfully created.')
    @api.expect(user_with_password)
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
@api.response(404, 'User not found.')
class UserItem(Resource):

    @api.marshal_with(user)
    def get(self, id):
        """
        Returns a category with a list of posts.
        """
        return User.query.filter(User.id == id).one()

    @api.expect(user)
    @api.response(204, 'User successfully updated.')
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

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes user.
        """
        delete_user(id)
        return None, 204
