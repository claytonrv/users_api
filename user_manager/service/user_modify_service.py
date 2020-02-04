from flask import request
from flask_restful import Resource
from data import UserDataHandler
from util import UserTranslator

class UserModifyService(Resource):
    def __init__(self, **kwargs):
       self.user_handler = UserDataHandler(kwargs['database_connector'])
       self.translator = UserTranslator()

    def post(self):
        user_json = request.json
        user = self.translator.translate_json_to_user(user_json)
        return self.user_handler.update_user(user)