import werkzeug
from sys import path
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint, 
    version=0.1,
    title='Cryptocity API',
    description='An api for cryptocurries and crypto-portifolio info'
)

api.add_namespace(user_ns, path='/user')