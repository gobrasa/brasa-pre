import logging

from flask import request
from flask_cors import cross_origin
from flask_restplus import Resource, Namespace, fields

from database.models import Mentee, MenteeSchema
from restful_api.db_ops.business import create_mentee, delete_from_table, \
    update_mentee, retrieve_single_item_with_filter, return_elements_using_schema
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

@ns.route('/')
class MenteeCollection(Resource):

    #@ns.marshal_list_with(mentee)
    #@cross_origin(supports_credentials=True)
    # ToDo - change back to line above if CORS does not work
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        Returns list of mentees.
        """
        mentees = Mentee.query.all()
        return return_elements_using_schema(mentees, MenteeSchema, many=True)


    @ns.response(201, 'Category successfully created.')
    @ns.expect(mentee)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new mentee.
        """
        data = request.json
        create_mentee(data)
        return '', 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class MenteeItemByUsername(Resource):

    #@ns.marshal_with(mentee)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, username):
        """
        Returns a mentee by username.
        """

        return retrieve_single_item_with_filter(Mentee, MenteeSchema, {'username': username})


@ns.route('/<int:id>')
@ns.response(404, 'User not found.')
class MenteeItem(Resource):

    #@ns.marshal_with(mentee)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, id):
        """
        Returns a mentee by ID.
        """
        return retrieve_single_item_with_filter(Mentee, MenteeSchema,{'id': id})

    #@ns.expect(mentee)
    @ns.response(204, 'Mentee successfully updated.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def put(self, id):

        data = request.json
        id = update_mentee(id, data)
        return str(id), 204

    @ns.response(204, 'User successfully deleted.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def delete(self, id):
        """
        Deletes user.
        """
        delete_from_table(Mentee, id)
        return None, 204
