from flask_restplus import fields

from restful_api.endpoints import api

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})





exam_schedule = api.model('Exam_Schedules', {
    'id': fields.Integer('id'),
    'realization_date': fields.DateTime(readOnly=True, description='realization date'),
    'mentee_id': fields.Integer(readOnly=True, description='mentee_id'),
    'exam_id':fields.Integer(readOnly=True, description='exam_id'),
    'score': fields.String(readOnly=True, description='score')
})
