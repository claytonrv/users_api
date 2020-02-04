from flask_restful import Resource
from data import UserDataHandler
from util import UserTranslator
import json

class UserListService(Resource):
    def __init__(self, **kwargs):
       self.user_handler = UserDataHandler(kwargs['database_connector'])
       self.translator = UserTranslator()

    def get(self, user_id):
        jsonsList = json.dumps(self.user_handler.retrieve(user_id), default=self.translator.object_dict)
        return json.loads(jsonsList)

        

