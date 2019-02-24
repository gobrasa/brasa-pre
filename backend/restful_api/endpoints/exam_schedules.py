import logging

from flask import request
from flask_cors import cross_origin
from flask_restplus import Namespace, Resource, fields

from database.models import ExamSchedule, ExamScheduleSchema, Mentee
from restful_api.db_ops.business import delete_from_table, create_exam_schedule, update_exam_schedule, \
    return_elements_using_schema, retrieve_single_item_with_filter

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

    #@ns.marshal_list_with(exam_schedule)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        Returns list of exam schedules.
        """
        exam_schedules = ExamSchedule.query.all()
        return return_elements_using_schema(exam_schedules, ExamScheduleSchema, many=True)

    @ns.response(201, 'ExamSchedule successfully created.')
    @ns.expect(exam_schedule)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new exam_schedule.
        """
        data = request.json
        create_exam_schedule(data)
        return '', 201

@ns.route('/<string:username>')
@ns.response(404, 'username not found')
class ExamScheduleItemByUsername(Resource):

    #@ns.marshal_with(exam_schedule)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, username):
        """
        Returns list of exam_schedule by username.
        """

        mentee = Mentee.query.filter(Mentee.username == username).one()
        exam_schedules = ExamSchedule.query.filter(ExamSchedule.mentee_id == mentee.id).all()

        return return_elements_using_schema(exam_schedules, ExamScheduleSchema,many=True)

@ns.route('/<int:id>')
@ns.response(404, 'ID not found.')
class ExamScheduleItem(Resource):

    #@ns.marshal_with(exam_schedule)
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self, id):
        """
        Returns an exam_schedule by ID.
        """

        return retrieve_single_item_with_filter(ExamSchedule, ExamScheduleSchema, {'id': id})

    @ns.expect(exam_schedule)
    @ns.response(204, 'ExamSchedule successfully updated.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def put(self, id):
        """
        Updates a mentor.
        """
        data = request.json
        update_exam_schedule(id, data)
        return '', 204

    @ns.response(204, 'ExamSchedule successfully deleted.')
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def delete(self, id):
        """
        Deletes mentor.
        """
        delete_from_table(ExamSchedule, id)
        return '', 204
