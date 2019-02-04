from flask_restplus import fields
from api.restplus import api



pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})



category = api.model('Blog category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
    'name': fields.String(required=True, description='Category name'),
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
    'mentor_id':fields.Integer(readOnly=True, description='mentor_id'),
    'username':fields.String(readOnly=True, description='username'),
    'first_name': fields.String(readOnly=True, description='first_name'),
    'last_name': fields.String(readOnly=True, description='last_name'),
    'city': fields.String(readOnly=True, description='city'),
    'state': fields.String(readOnly=True, description='state'),
    'financial_aid': fields.Boolean(description='financial_aid'),
    'cycle_id': fields.Integer(description='cycle_id')
})