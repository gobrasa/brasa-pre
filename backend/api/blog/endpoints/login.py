import logging

from flask import request
from flask_restplus import Resource

from api.Exceptions import RoleNotAllowedException
from api.blog.business import create_user, delete_user, update_user
from api.blog.serializers import user, user_with_password, user_and_pw
from api.restplus import api
from database.models import User
from werkzeug.security import generate_password_hash, check_password_hash
log = logging.getLogger(__name__)

ns = api.namespace('ops', description='Operations related to logins')

@ns.route('/is_authenticated/<string:username>')
@api.response(404, 'user not found')
class IsAuthenticated(Resource):

    def get(self, username):
        user = User.query.filter(User.username == username).first_or_404()
        return user.authenticated

@ns.route('/login')
class Login2Colle(Resource):

    @api.response(404, 'user not found')
    @api.response(401, 'unauthorized')
    @api.expect(user_and_pw)
    def post(self):
        """ Logs password in if exists """
        input = request.get_json()
        username, password = input['username'], input['password']
        user = User.query.filter(User.username == username).first_or_404()

        print (password)

        if not check_password_hash(user.password_hash, password):
            return 'Wrong password', 401

        user.authenticated = True
        User.query.session.add(user)
        User.query.session.commit()

        return 'User logged in', 200

@ns.route('/logout')
class LogoutCollection(Resource):

    @api.response(404, 'user not found')
    @api.expect(user_and_pw)
    def post(self):
        """ Logs out user in if exists """
        input = request.get_json()
        user = User.query.filter(User.username == input['username']).first_or_404()
        user.authenticated = False

        User.query.session.add(user)
        User.query.session.commit()

        return 'User logged out', 200

@ns.route('/')
class LoginCollection(Resource):

    @api.marshal_list_with(user)
    def get(self):
        """
        Returns list of blog categories.
        """
        users = User.query.all()
        return users

    @api.response(201, 'Category successfully created.')
    @api.expect(user_with_password)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        try:
            create_user(data)
        except RoleNotAllowedException as ex:
            return 'Role not recognized. ' \
                   'Exception: {},' \
                   'Errors: {}'.format(ex, ex.errors), 400
        return None, 201