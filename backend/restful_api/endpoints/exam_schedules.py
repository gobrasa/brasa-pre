import logging

from flask import request
from flask_restplus import Namespace, Resource, fields

from database.models import ExamSchedule
from restful_api.business import delete_from_table, create_exam_schedule, update_exam_schedule

log = logging.getLogger(__name__)

ns = Namespace('exam_schedules', description='Operations related to exam_schedules')

exam_schedule = ns.model('Exam_Schedules', {
    'id': fields.Integer,
    'realization_date': fields.DateTime(required=True, description='realization date'),
    'mentee_id': fields.Integer(required=True, description='mentee_id'),
    'exam_id':fields.Integer(required=True, description='exam_id'),
    'score': fields.String(required=True, description='score')
})


@ns.route('/')
class ExamSchedulesCollection(Resource):

    @ns.marshal_list_with(exam_schedule)
    def get(self):
        """
        Returns list of exam schedules.
        """
        exam_schedules = ExamSchedule.query.all()
        return exam_schedules

    @ns.response(201, 'ExamSchedule successfully created.')
    @ns.expect(exam_schedule)
    def post(self):
        """
        Creates a new exam_schedule.
        """
        data = request.json
        create_exam_schedule(data)
        return None, 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class ExamScheduleItemByUsername(Resource):

    @ns.marshal_with(exam_schedule)
    def get(self, username):
        """
        Returns list of exam_schedule by username.
        """
        return ExamSchedule.query.filter(ExamSchedule.username == username).all()

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class ExamScheduleItem(Resource):

    @ns.marshal_with(exam_schedule)
    def get(self, id):
        """
        Returns an exam_schedule by ID.
        """
        return ExamSchedule.query.filter(ExamSchedule.id == id).one()

    @ns.expect(exam_schedule)
    @ns.response(204, 'ExamSchedule successfully updated.')
    def put(self, id):
        """
        Updates a mentor.
        """
        data = request.json
        update_exam_schedule(id, data)
        return None, 204

    @ns.response(204, 'ExamSchedule successfully deleted.')
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(ExamSchedule, id)
        return None, 204
