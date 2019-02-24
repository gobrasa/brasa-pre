import logging

from flask import request, jsonify
from flask_cors import cross_origin
from flask_restplus import Resource, Namespace, fields

from auth.auth import requires_auth
from database.models import Exams, ExamsSchema
from restful_api.db_ops.business import delete_from_table, create_exam, update_exam

log = logging.getLogger(__name__)

ns = Namespace('exams', description='Operations related to exams')

exam = ns.model('Exams', {
    'id': fields.Integer,
    'category': fields.String(readOnly=True, description='category'),
    'subcategory': fields.String(readOnly=True, description='subcategory')
})


@ns.route('/')
class ExamCollection(Resource):

    @cross_origin(headers=['Content-Type', 'Authorization'])
    #@requires_auth
    #@ns.doc(security='apikey')
    def get(self):
        """
        Returns list of exam schedules.
        """
        print('entered get exams')
        exams = Exams.query.all()
        exams_schema = ExamsSchema(many=True)
        result = exams_schema.dump(exams)
        return jsonify(result.data)



    #@ns.response(201, 'Exam successfully created.')
    #@ns.expect(exam)
    #@requires_auth
    #@cross_origin(headers=['Content-Type', 'Authorization'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        Creates a new exam.
        """
        print('entered post exam')
        data = request.json
        exam_id = create_exam(data)
        print(exam_id)
        return jsonify(exam_id), 201

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
