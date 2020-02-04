To run this the application you may start using a virtual env to get thing easyier, to do this run the following commands(Considering that you hava python and pip installed):

$ pip install virtualenv

$ virtualenv venv 

$ source venv/bin/activate

Now install the requirements:

$ pip install -r user_manager/requirements.txt

Change the file (user_api.py) on line 9 inserting you database information.

Use the file tables_creation.sql to create the database and tables nedded

To start the application, you'll run:

$ python user_api.py


To use the application:

Register user:
Method: PUT 
URL: localhost:5000/user/register
json: {
	"name":"Clayton Veras",
	"document":"0987654321",
	"email":"mayara@email.com",
	"birth_date":"1994-07-14"
}

Retrieve User:
Method: GET
URL: localhost:5000/user/<id_user>

Retrieve all users:
Method: GET
URL: localhost:5000/user/0

Change User:
Method: POST
URL: localhost:5000/user/change
json: {
	"name":"Clayton R, Veras",
	"document":"0987654321",
	"email":"mayara@email.com",
	"birth_date":"1994-07-14"
}

Delete User: 
Method: DELETE
URL: localhost:5000/user/delete/<id_user>
