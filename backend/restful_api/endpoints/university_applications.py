import logging

from flask import request
from flask_cors import cross_origin
from flask_restplus import Resource, Namespace, fields

from database.models import UniversityApplication, UniversityApplicationSchema
from restful_api.db_ops.business import delete_from_table, create_university_application, update_university_application, \
    create_university_application_for_mentee, return_elements_using_schema, retrieve_single_item_with_filter

log = logging.getLogger(__name__)

ns = Namespace('university_applications', description='Operations related to uploads')

university_application = ns.model('UniversityApplication_application', {
    'id': fields.Integer,
    'mentee_id': fields.String('name'),
    'university_id': fields.String('name')
})

university_list_def = ns.model('UniversityListFromMentee', {
    'universities': fields.List(fields.Integer, description='list of universities',required=True)
})

@ns.route('/')
class UniversityApplicationCollection(Resource):

    #@ns.marshal_list_with(university_application)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        Returns list of uploads.
        """
        university_apps = UniversityApplication.query.all()
        return return_elements_using_schema(university_apps, UniversityApplicationSchema, many=True)

    @ns.response(201, 'UniversityApplication successfully created.')
    @ns.expect(university_application)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new upload.
        """
        data = request.json
        create_university_application(data)
        return '', 201

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class UniversityApplicationItem(Resource):

    #@ns.marshal_with(university_application)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, id):
        """
        Returns an upload by ID.
        """
        return retrieve_single_item_with_filter(UniversityApplication, UniversityApplicationSchema,
                                                {'id': id})

    @ns.expect(university_application)
    @ns.response(204, 'UniversityApplication successfully updated.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def put(self, id):
        """
        Updates an upload.
        """
        data = request.json
        update_university_application(id, data)
        return '', 204

    @ns.response(204, 'UniversityApplication successfully deleted.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(UniversityApplication, id)
        return '', 204

@ns.route('/university_applications_mentee/<int:mentee_id>')
@ns.response(404, 'ID not found.')
class UniversityApplicationListForMentee(Resource):

    @ns.response(201, 'UniversityApplication successfully created.')
    @ns.expect(university_list_def)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self, mentee_id):
        """
        Creates a new upload.
        """
        data = request.json
        university_ids = data['universities']
        print(university_ids)
        create_university_application_for_mentee(mentee_id, university_ids)
        return '', 201
