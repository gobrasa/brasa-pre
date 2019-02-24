import logging

from flask import request
from flask_cors import cross_origin
from flask_restplus import Resource, Namespace, fields

from database.models import University, UniversitySchema
from restful_api.db_ops.business import delete_from_table, update_university, create_university, \
    return_elements_using_schema, retrieve_single_item_with_filter

log = logging.getLogger(__name__)

ns = Namespace('universities', description='Operations related to uploads')

university = ns.model('University', {
    'id': fields.Integer,
    'name': fields.String('name'),
    'city': fields.String('name'),
    'state': fields.String('name'),
    'country_iso_code': fields.String('country_iso_code')
})


@ns.route('/')
class UniversityCollection(Resource):

    #@ns.marshal_list_with(university)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        Returns list of uploads.
        """
        universities = University.query.all()
        return return_elements_using_schema(universities, UniversitySchema, many=True)

    @ns.response(201, 'University successfully created.')
    @ns.expect(university)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_university(data)
        return '', 201

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class UniversityItem(Resource):

    #@ns.marshal_with(university)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, id):
        """
        Returns an upload by ID.
        """
        #return University.query.filter(University.id == id).one()

        return retrieve_single_item_with_filter(University, UniversitySchema, {'id': id})

    @ns.expect(university)
    @ns.response(204, 'University successfully updated.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_university(id, data)
        return '', 204

    @ns.response(204, 'University successfully deleted.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(University, id)
        return '', 204
