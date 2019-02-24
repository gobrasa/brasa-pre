import logging

from flask import request
from flask_cors import cross_origin
from flask_restplus import Resource, Namespace, fields

from database.models import Uploads, UploadsSchema
from restful_api.db_ops.business import delete_from_table, create_upload, update_upload, \
    retrieve_single_item_with_filter, return_elements_using_schema

log = logging.getLogger(__name__)

ns = Namespace('uploads', description='Operations related to uploads')

upload = ns.model('Uploads', {
    'id': fields.Integer,
    'link': fields.String(readOnly=True, description='link to a file in Google Drive'),
    'username': fields.String(readOnly=True, description='username')
})


@ns.route('/')
class UploadsCollection(Resource):

    #@ns.marshal_list_with(upload)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        Returns list of uploads.
        """
        uploads = Uploads.query.all()
        return return_elements_using_schema(uploads, UploadsSchema, many=True)

    @ns.response(201, 'Upload successfully created.')
    @ns.expect(upload)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_upload(data)
        return '', 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class UploadItemByUsername(Resource):

    #@ns.marshal_with(upload)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, username):
        """
        Returns list of uploads by username.
        """
        uploads = Uploads.query.filter(Uploads.username == username).all()
        return return_elements_using_schema(uploads, UploadsSchema, many=True)

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class UploadItem(Resource):

    #@ns.marshal_with(upload)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, id):
        """
        Returns an upload by ID.
        """
        return retrieve_single_item_with_filter(Uploads, UploadsSchema, {'upload_id': id})

    @ns.expect(upload)
    @ns.response(204, 'Upload successfully updated.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_upload(id, data)
        return '', 204

    @ns.response(204, 'Upload successfully deleted.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(Uploads, id)
        return '', 204
