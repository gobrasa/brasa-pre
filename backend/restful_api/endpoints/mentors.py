import logging

from flask import request, jsonify
from flask_cors import cross_origin
from flask_restplus import Resource, Namespace, fields

from database.models import Mentor, MentorSchema
from restful_api.db_ops.business import delete_from_table, update_mentor, create_mentor, \
    retrieve_single_item_with_filter, return_elements_using_schema

log = logging.getLogger(__name__)

ns = Namespace('mentors', description='Operations related to mentors')

cycle = ns.model('Cycle', {
    'id': fields.Integer,
    'summary': fields.String('summary'),
    'cycle_start': fields.DateTime('cycle_start'),
    'cycle_end': fields.DateTime('cycle_end'),
    'region': fields.String('region')
})

mentor = ns.model('Mentor', {
    'id': fields.Integer,
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'cycle_id': fields.Integer(description='cycle_id'),
    'cycle': fields.Nested(cycle)
})


@ns.route('/')
class MentorCollection(Resource):

    #@ns.marshal_list_with(mentor)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        Returns list of mentors.
        """
        mentors = Mentor.query.all()
        return return_elements_using_schema(mentors, MentorSchema, many=True)


    @ns.response(201, 'Mentor successfully created.')
    @ns.expect(mentor)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new mentor.
        """
        data = request.json
        create_mentor(data)
        return '', 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class MentorItemByUsername(Resource):

    #@ns.marshal_with(mentor)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, username):
        """
        Returns a mentor by username.
        """

        return retrieve_single_item_with_filter(Mentor, MentorSchema, {'username': username})

@ns.route('/<int:id>')
@ns.response(404, 'User not found.')
class MentorItem(Resource):

    #@ns.marshal_with(mentor)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, id):
        """
        Returns a mentor by ID.
        """
        return retrieve_single_item_with_filter(Mentor, MentorSchema, {'id': id})

    @ns.expect(mentor)
    @ns.response(204, 'Mentee successfully updated.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def put(self, id):
        """
        Updates a mentor.
        """
        data = request.json
        update_mentor(id, data)
        return '', 204

    @ns.response(204, 'User successfully deleted.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(Mentor, id)
        return '', 204
