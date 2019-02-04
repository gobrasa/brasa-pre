import logging

from flask import request
from flask_restplus import Resource

from api.business import create_mentee, delete_from_table, \
    update_mentee
from api.serializers import mentee
from api.restplus import api
from database.models import Mentee

log = logging.getLogger(__name__)

ns = api.namespace('mentees', description='Operations related to mentees')

# ToDo - check if it is a good idea to add basic_role_auth and load users from env variables
#auth = BasicRoleAuth()
#auth.add_user(user=os.getenv('ADMIN_USERNAME'), password=os.getenv('ADMIN_PW'), roles='admin')

@ns.route('/')
class MenteeCollection(Resource):

    @api.marshal_list_with(mentee)
    def get(self):
        """
        Returns list of mentees.
        """
        users = Mentee.query.all()
        return users

    @api.response(201, 'Category successfully created.')
    @api.expect(mentee)
    def post(self):
        """
        Creates a new mentee.
        """
        data = request.json
        create_mentee(data)
        return None, 201

@ns.route('/<string:username>')
@api.response(404, 'username not found')
class MenteeItemByUsername(Resource):

    @api.marshal_with(mentee)
    def get(self, username):
        """
        Returns a mentee by username.
        """
        return Mentee.query.filter(Mentee.username == username).one()

@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class MenteeItem(Resource):

    @api.marshal_with(mentee)
    def get(self, id):
        """
        Returns a mentee by ID.
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
