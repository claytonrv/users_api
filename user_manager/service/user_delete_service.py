from flask import request
from flask_restful import Resource
from data import UserDataHandler

class UserDeleteService(Resource):
    def __init__(self, **kwargs):
       self.user_handler = UserDataHandler(kwargs['database_connector'])

    def delete(self, user_id):
        return self.user_handler.delete(user_id)