import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from database.models import Mentee, Mentor
from restful_api.business import delete_from_table, update_mentor, create_mentor

log = logging.getLogger(__name__)

ns = Namespace('mentors', description='Operations related to mentors')

cycle = ns.model('Cycle', {
    'id': fields.Integer('id'),
    'summary': fields.String('summary'),
    'cycle_start': fields.DateTime('cycle_start'),
    'cycle_end': fields.DateTime('cycle_end'),
    'region': fields.String('region')
})

mentor = ns.model('Mentor', {
    'id': fields.Integer('id'),
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'cycle_id': fields.Integer(description='cycle_id'),
    'cycle': fields.Nested(cycle)
})


@ns.route('/')
class MentorCollection(Resource):

    @ns.marshal_list_with(mentor)
    def get(self):
        """
        Returns list of mentors.
        """
        mentors = Mentor.query.all()
        return mentors

    @ns.response(201, 'Mentor successfully created.')
    @ns.expect(mentor)
    def post(self):
        """
        Creates a new mentor.
        """
        data = request.json
        create_mentor(data)
        return None, 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class MentorItemByUsername(Resource):

    @ns.marshal_with(mentor)
    def get(self, username):
        """
        Returns a mentor by username.
        """
        return Mentor.query.filter(Mentor.username == username).one()

@ns.route('/<int:id>')
@ns.response(404, 'User not found.')
class MentorItem(Resource):

    @ns.marshal_with(mentor)
    def get(self, id):
        """
        Returns a mentor by ID.
        """
        return Mentee.query.filter(Mentor.id == id).one()

    @ns.expect(mentor)
    @ns.response(204, 'Mentee successfully updated.')
    def put(self, id):
        """
        Updates a mentor.
        """
        data = request.json
        update_mentor(id, data)
        return None, 204

    @ns.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(Mentor, id)
        return None, 204
