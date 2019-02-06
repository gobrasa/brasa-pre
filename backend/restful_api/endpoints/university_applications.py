import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from database.models import UniversityApplication
from restful_api.business import delete_from_table, create_university_application, update_university_application, \
    create_university_application_for_mentee

log = logging.getLogger(__name__)

ns = Namespace('university_applications', description='Operations related to uploads')

university_application = ns.model('UniversityApplication_application', {
    'id': fields.Integer,
    'mentee_id': fields.String('name'),
    'university_id': fields.String('name')
})

university_list_def = ns.model('UniversityListFromMentee', {
    'universities': fields.List(fields.String, description='list of universities',required=True)
})

@ns.route('/')
class UniversityApplicationCollection(Resource):

    @ns.marshal_list_with(university_application)
    def get(self):
        """
        Returns list of uploads.
        """
        uploads = UniversityApplication.query.all()
        return uploads

    @ns.response(201, 'UniversityApplication successfully created.')
    @ns.expect(university_application)
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_university_application(data)
        return None, 201

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class UniversityApplicationItem(Resource):

    @ns.marshal_with(university_application)
    def get(self, id):
        """
        Returns an upload by ID.
        """
        return UniversityApplication.query.filter(UniversityApplication.id == id).one()

    @ns.expect(university_application)
    @ns.response(204, 'UniversityApplication successfully updated.')
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_university_application(id, data)
        return None, 204

    @ns.response(204, 'UniversityApplication successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(UniversityApplication, id)
        return None, 204

@ns.route('/university_applications_mentee/<int:mentee_id>')
@ns.response(404, 'ID not found.')
class UniversityApplicationListForMentee(Resource):

    @ns.response(201, 'UniversityApplication successfully created.')
    @ns.expect(university_list_def)
    def post(self, mentee_id):
        """
        Creates a new upload.
        """
        data = request.json
        university_ids = data['universities']
        print(university_ids)
        create_university_application_for_mentee(mentee_id, university_ids)
        return None, 201