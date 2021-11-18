from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import get_user_by_id, get_users, create_user

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_all_users')
    @api.marshal_list_with(_user, envelope='users')
    def get(self):
        """List all users"""
        return get_users()

    @api.response(201, 'User successfully created')
    @api.doc('create_new_user')
    @api.expect(_user, validate=True)
    def post(self):
        """Create a new user"""
        data = request.json
        return create_user(data=data)

@api.route('/<public_id>')
class User(Resource):
    @api.doc('get_user_by_public_id')
    @api.marshal_with(_user, envelope='user')
    def get(self, public_id):
        """Get a user by public_id"""
        user = get_user_by_id(public_id=public_id)

        if not user:
            api.abort(404, 'User not found')
        return user
    