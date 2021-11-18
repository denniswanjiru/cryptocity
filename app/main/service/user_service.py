import uuid
import datetime

from flask.app import Flask

from app.main import db
from app.main.model.user import User

def save_and_commit(data):
    db.session.add(data)
    db.session.commit()

def create_user(data):
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        new_user = User(
            public_id = str(uuid.uuid4()),
            email=data['email'],
            password=data['password'],
            username=data['username'],
            created_at=datetime.datetime.utcnow()
        )

        save_and_commit(new_user)

        response_obj = {
            'success': True,
            'message': 'User created successfully'
        }
    
        return response_obj, 201
    else:
        response_obj = {
            'success': False,
            'message': 'User already exists. Please login.'
        }

        return response_obj, 409


def get_users():
    return User.query.all()

def get_user_by_id(public_id):
    return User.query.filter_by(public_id=public_id).first()
