from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from service import UserListService, UserModifyService, UserInsertService, UserDeleteService
from util import MySQLConnector

app = Flask(__name__)
api = Api(app)

connector = MySQLConnector(host='localhost', database='user_manager', port='3306', user='root', password='Admin@1234')
connector.connect()

api.add_resource(UserListService,'/user/<string:user_id>', resource_class_kwargs={'database_connector': connector.con})
api.add_resource(UserInsertService, '/user/register', resource_class_kwargs={'database_connector': connector.con})
api.add_resource(UserModifyService, '/user/change', resource_class_kwargs={'database_connector': connector.con})
api.add_resource(UserDeleteService, '/user/delete/<string:user_id>', resource_class_kwargs={'database_connector': connector.con})

if __name__ == '__main__':
    app.run(debug=True)