import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from auth.auth import requires_auth
from database.models import Exams
from restful_api.business import delete_from_table, create_exam, update_exam

log = logging.getLogger(__name__)

ns = Namespace('exams', description='Operations related to exams')

exam = ns.model('Exams', {
    'id': fields.Integer,
    'category': fields.String(readOnly=True, description='category'),
    'subcategory': fields.String(readOnly=True, description='subcategory')
})

@ns.route('/')
class ExamCollection(Resource):

    @ns.marshal_list_with(exam)
    @requires_auth
    def get(self):
        """
        Returns list of exam schedules.
        """
        exams = Exams.query.all()
        return exams

    @ns.response(201, 'Exam successfully created.')
    @ns.expect(exam)
    def post(self):
        """
        Creates a new exam_schedule.
        """
        data = request.json
        create_exam(data)
        return None, 201

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class ExamItem(Resource):

    @ns.marshal_with(exam)
    def get(self, id):
        """
        Returns an exam by ID.
        """
        return Exams.query.filter(Exams.id == id).one()

    @ns.expect(exam)
    @ns.response(204, 'Exam successfully updated.')
    def put(self, id):
        """
        Updates an exam.
        """
        data = request.json
        update_exam(id, data)
        return None, 204

    @ns.response(204, 'Exam successfully deleted.')
    def delete(self, id):
        """
        Deletes exam.
        """
        delete_from_table(Exams, id)
        return None, 204
