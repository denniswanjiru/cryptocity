from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='User related operations')

    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })