import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from database.models import Uploads
from restful_api.business import delete_from_table, create_upload, update_upload

log = logging.getLogger(__name__)

ns = Namespace('uploads', description='Operations related to uploads')

upload = ns.model('Uploads', {
    'id': fields.Integer('id'),
    'link': fields.String(readOnly=True, description='link to a file in Google Drive'),
    'username': fields.String(readOnly=True, description='username')
})


@ns.route('/')
class UploadsCollection(Resource):

    @ns.marshal_list_with(upload)
    def get(self):
        """
        Returns list of uploads.
        """
        uploads = Uploads.query.all()
        return uploads

    @ns.response(201, 'Upload successfully created.')
    @ns.expect(upload)
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_upload(data)
        return None, 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class UploadItemByUsername(Resource):

    @ns.marshal_with(upload)
    def get(self, username):
        """
        Returns list of uploads by username.
        """
        return Uploads.query.filter(Uploads.username == username).all()

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class UploadItem(Resource):

    @ns.marshal_with(upload)
    def get(self, id):
        """
        Returns an upload by ID.
        """
        return Uploads.query.filter(Uploads.id == id).one()

    @ns.expect(upload)
    @ns.response(204, 'Upload successfully updated.')
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_upload(id, data)
        return None, 204

    @ns.response(204, 'Upload successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(Uploads, id)
        return None, 204
