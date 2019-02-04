import logging

from flask import request
from flask_restplus import Resource

from api.business import delete_from_table, create_upload, update_upload, create_exam, update_exam
from api.restplus import api
from api.serializers import upload, exam_schedule, exam
from database.models import Uploads, Exams

log = logging.getLogger(__name__)

ns = api.namespace('exams', description='Operations related to exams')


@ns.route('/')
class ExamCollection(Resource):

    @api.marshal_list_with(exam)
    def get(self):
        """
        Returns list of exam schedules.
        """
        exams = Exams.query.all()
        return exams

    @api.response(201, 'Exam successfully created.')
    @api.expect(exam)
    def post(self):
        """
        Creates a new exam_schedule.
        """
        data = request.json
        create_exam(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'ID not found.')
class ExamItem(Resource):

    @api.marshal_with(exam)
    def get(self, id):
        """
        Returns an exam by ID.
        """
        return Exams.query.filter(Exams.id == id).one()

    @api.expect(exam)
    @api.response(204, 'Exam successfully updated.')
    def put(self, id):
        """
        Updates an exam.
        """
        data = request.json
        update_exam(id, data)
        return None, 204

    @api.response(204, 'Exam successfully deleted.')
    def delete(self, id):
        """
        Deletes exam.
        """
        delete_from_table(Exams, id)
        return None, 204
