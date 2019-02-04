import logging

from flask import request
from flask_restplus import Resource

from api.Exceptions import RoleNotAllowedException
from api.blog.business import create_user, delete_user, update_user, create_mentee, delete_from_table, \
    update_mentee
from api.blog.serializers import category, user, user_with_password, mentee
from api.restplus import api
from database.models import User, Mentee

log = logging.getLogger(__name__)

ns = api.namespace('mentees', description='Operations related to mentees')


@ns.route('/')
class MenteeCollection(Resource):

    @api.marshal_list_with(mentee)
    def get(self):
        """
        Returns list of blog categories.
        """
        users = Mentee.query.all()
        return users

    @api.response(201, 'Category successfully created.')
    @api.expect(mentee)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        create_mentee(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class MenteeItem(Resource):

    @api.marshal_with(mentee)
    def get(self, id):
        """
        Returns a category with a list of posts.
        """
        return Mentee.query.filter(Mentee.id == id).one()

    @api.expect(mentee)
    @api.response(204, 'Mentee successfully updated.')
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
        update_mentee(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes user.
        """
        delete_from_table(Mentee, id)
        return None, 204
