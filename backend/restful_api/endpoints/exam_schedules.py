import logging

from flask import request
from flask_restful import fields
from flask_restplus import Namespace, Resource

from database.models import ExamSchedule
from restful_api.business import delete_from_table, create_exam_schedule, update_exam_schedule

log = logging.getLogger(__name__)

ns = Namespace('exam_schedules', description='Operations related to exam_schedules')

exam_schedule = ns.model('Exam_Schedules', {
    'id': fields.Integer('id'),
    'realization_date': fields.DateTime(readOnly=True, description='realization date'),
    'mentee_id': fields.Integer(readOnly=True, description='mentee_id'),
    'exam_id':fields.Integer(readOnly=True, description='exam_id'),
    'score': fields.String(readOnly=True, description='score')
})


@ns.route('/')
class ExamSchedulesCollection(Resource):

    @api.marshal_list_with(exam_schedule)
    def get(self):
        """
        Returns list of exam schedules.
        """
        exam_schedules = ExamSchedule.query.all()
        return exam_schedules

    @api.response(201, 'ExamSchedule successfully created.')
    @api.expect(exam_schedule)
    def post(self):
        """
        Creates a new exam_schedule.
        """
        data = request.json
        create_exam_schedule(data)
        return None, 201

@ns.route('/<string:username>')
@api.response(404, 'username not found')
class ExamScheduleItemByUsername(Resource):

    @api.marshal_with(exam_schedule)
    def get(self, username):
        """
        Returns list of exam_schedule by username.
        """
        return ExamSchedule.query.filter(ExamSchedule.username == username).all()

@ns.route('/<int:id>')
@api.response(404, 'ID not found.')
class ExamScheduleItem(Resource):

    @api.marshal_with(exam_schedule)
    def get(self, id):
        """
        Returns an exam_schedule by ID.
        """
        return ExamSchedule.query.filter(ExamSchedule.id == id).one()

    @api.expect(exam_schedule)
    @api.response(204, 'ExamSchedule successfully updated.')
    def put(self, id):
        """
        Updates a mentor.
        """
        data = request.json
        update_exam_schedule(id, data)
        return None, 204

    @api.response(204, 'ExamSchedule successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(ExamSchedule, id)
        return None, 204
