import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from database.models import University
from restful_api.business import delete_from_table, create_upload, update_upload, update_university, create_university

log = logging.getLogger(__name__)

ns = Namespace('universities', description='Operations related to uploads')

university = ns.model('University', {
    'id': fields.Integer('id'),
    'name': fields.String('name'),
    'city': fields.String('name'),
    'state': fields.String('name'),
    'country_iso_code': fields.String('country_iso_code')
})


@ns.route('/')
class UniversityCollection(Resource):

    @ns.marshal_list_with(university)
    def get(self):
        """
        Returns list of uploads.
        """
        uploads = University.query.all()
        return uploads

    @ns.response(201, 'University successfully created.')
    @ns.expect(university)
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_university(data)
        return None, 201

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class UniversityItem(Resource):

    @ns.marshal_with(university)
    def get(self, id):
        """
        Returns an upload by ID.
        """
        return University.query.filter(University.id == id).one()

    @ns.expect(university)
    @ns.response(204, 'University successfully updated.')
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_university(id, data)
        return None, 204

    @ns.response(204, 'University successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(University, id)
        return None, 204
