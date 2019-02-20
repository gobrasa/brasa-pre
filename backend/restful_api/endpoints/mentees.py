import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from auth.auth import requires_auth
from database.models import Mentee
from restful_api.business import create_mentee, delete_from_table, \
    update_mentee
from restful_api.endpoints.universities import university

log = logging.getLogger(__name__)

ns = Namespace('mentees', description='Operations related to mentees')


university_application = ns.model('University_Application', {
    'id': fields.Integer,
    'mentee_id':fields.Integer('mentee_id'),
    'university_id':fields.Integer('university_id'),
    'university': fields.Nested(university)
})


mentee = ns.model('Mentee', {
    'id': fields.Integer('id'),
    'mentor_id':fields.Integer(readOnly=True, description='mentor_id'),
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'city': fields.String(readOnly=True, description='city'),
    'state': fields.String(readOnly=True, description='state'),
    'financial_aid': fields.Boolean(description='financial_aid'),
    'cycle_id': fields.Integer(description='cycle_id'),
    'university_applications':fields.List(fields.Nested(university_application))

})

# ToDo - check if it is a good idea to add basic_role_auth and load users from env variables
#auth = BasicRoleAuth()
#auth.add_user(user=os.getenv('ADMIN_USERNAME'), password=os.getenv('ADMIN_PW'), roles='admin')

@ns.route('/')
class MenteeCollection(Resource):

    @ns.marshal_list_with(mentee)
    def get(self):
        """
        Returns list of mentees.
        """
        users = Mentee.query.all()
        return users

    @ns.response(201, 'Category successfully created.')
    @ns.expect(mentee)
    def post(self):
        """
        Creates a new mentee.
        """
        data = request.json
        create_mentee(data)
        return None, 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class MenteeItemByUsername(Resource):

    @ns.marshal_with(mentee)
    def get(self, username):
        """
        Returns a mentee by username.
        """
        return Mentee.query.filter(Mentee.username == username).one()

@ns.route('/<int:id>')
@ns.response(404, 'User not found.')
class MenteeItem(Resource):

    @ns.marshal_with(mentee)
    def get(self, id):
        """
        Returns a mentee by ID.
        """
        return Mentee.query.filter(Mentee.id == id).one()

    @ns.expect(mentee)
    @ns.response(204, 'Mentee successfully updated.')
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

    @ns.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes user.
        """
        delete_from_table(Mentee, id)
        return None, 204
