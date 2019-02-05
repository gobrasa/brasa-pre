import logging

from flask import request
from flask_restful import fields
from flask_restplus import Resource, Namespace

from database.models import Mentee, Mentor
from restful_api.business import delete_from_table

log = logging.getLogger(__name__)

ns = Namespace('mentors', description='Operations related to mentors')


mentor = ns.model('Mentor', {
    'id': fields.Integer('id'),
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'cycle_id': fields.Integer(description='cycle_id')
})


@ns.route('/')
class MentorCollection(Resource):

    @api.marshal_list_with(mentor)
    def get(self):
        """
        Returns list of mentors.
        """
        mentors = Mentor.query.all()
        return mentors

    @api.response(201, 'Mentor successfully created.')
    @api.expect(mentor)
    def post(self):
        """
        Creates a new mentor.
        """
        data = request.json
        create_mentor(data)
        return None, 201

@ns.route('/<string:username>')
@api.response(404, 'username not found')
class MentorItemByUsername(Resource):

    @api.marshal_with(mentor)
    def get(self, username):
        """
        Returns a mentor by username.
        """
        return Mentor.query.filter(Mentor.username == username).one()

@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class MentorItem(Resource):

    @api.marshal_with(mentor)
    def get(self, id):
        """
        Returns a mentor by ID.
        """
        return Mentee.query.filter(Mentor.id == id).one()

    @api.expect(mentor)
    @api.response(204, 'Mentee successfully updated.')
    def put(self, id):
        """
        Updates a mentor.
        """
        data = request.json
        update_mentor(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(Mentor, id)
        return None, 204
