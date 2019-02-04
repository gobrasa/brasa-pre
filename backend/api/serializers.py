from flask_restplus import fields
from api.restplus import api



pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})


user_and_pw = api.model('User2', {
    'username':fields.String(readOnly=True, description='username'),
    'password': fields.String(readOnly=True, description='password'),
})

user = api.model('User', {
    'id':fields.Integer(readOnly=True, description='id'),
    'username':fields.String(readOnly=True, description='username'),
    'email': fields.String(readOnly=True, description='email'),
    'role_name': fields.String(readOnly=True, description='role_name'),
    #'uploads': fieds.List(fields.Nested())
})

user_with_password = api.model('User', {
    'id':fields.Integer(readOnly=True, description='id'),
    'username':fields.String(readOnly=True, description='username'),
    'email': fields.String(readOnly=True, description='email'),
    'role_name': fields.String(readOnly=True, description='role_name'),
    'password': fields.String(readOnly=True, description='password'),
    #'uploads': fieds.List(fields.Nested())
})

mentee = api.model('Mentee', {
    'id': fields.Integer('id'),
    'mentor_id':fields.Integer(readOnly=True, description='mentor_id'),
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'city': fields.String(readOnly=True, description='city'),
    'state': fields.String(readOnly=True, description='state'),
    'financial_aid': fields.Boolean(description='financial_aid'),
    'cycle_id': fields.Integer(description='cycle_id')
})

mentor = api.model('Mentor', {
    'id': fields.Integer('id'),
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'cycle_id': fields.Integer(description='cycle_id')
})

upload = api.model('Uploads', {
    'id': fields.Integer('id'),
    'link': fields.String(readOnly=True, description='link to a file in Google Drive'),
    'username': fields.String(readOnly=True, description='username')
})

exam_schedule = api.model('Exam_Schedules', {
    'id': fields.Integer('id'),
    'realization_date': fields.DateTime(readOnly=True, description='realization date'),
    'mentee_id': fields.Integer(readOnly=True, description='mentee_id'),
    'exam_id':fields.Integer(readOnly=True, description='exam_id'),
    'score': fields.String(readOnly=True, description='score')
})

exam = api.model('Exams', {
    'id': fields.Integer('id'),
    'category': fields.String(readOnly=True, description='category'),
    'subcategory': fields.String(readOnly=True, description='subcategory')
})