import logging

from flask import request
from flask_restplus import Resource

from api.business import delete_from_table, create_upload, update_upload
from api.restplus import api
from api.serializers import upload
from database.models import Uploads

log = logging.getLogger(__name__)

ns = api.namespace('uploads', description='Operations related to uploads')


@ns.route('/')
class UploadsCollection(Resource):

    @api.marshal_list_with(upload)
    def get(self):
        """
        Returns list of uploads.
        """
        uploads = Uploads.query.all()
        return uploads

    @api.response(201, 'Upload successfully created.')
    @api.expect(upload)
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_upload(data)
        return None, 201

@ns.route('/<string:username>')
@api.response(404, 'username not found')
class UploadItemByUsername(Resource):

    @api.marshal_with(upload)
    def get(self, username):
        """
        Returns list of uploads by username.
        """
        return Uploads.query.filter(Uploads.username == username).all()

@ns.route('/<int:id>')
@api.response(404, 'ID not found.')
class UploadItem(Resource):

    @api.marshal_with(upload)
    def get(self, id):
        """
        Returns an upload by ID.
        """
        return Uploads.query.filter(Uploads.id == id).one()

    @api.expect(upload)
    @api.response(204, 'Upload successfully updated.')
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_upload(id, data)
        return None, 204

    @api.response(204, 'Upload successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(Uploads, id)
        return None, 204
