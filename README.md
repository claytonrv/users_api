To run this the application 
===========================

I suggest you to use a virtual env to get things working without break anything else. 
To do this, run the following commands(Considering that you have python and pip installed already):

```bash
$ pip install virtualenv

$ virtualenv venv 

$ source venv/bin/activate
```

Now install the requirements:

```bash
$ pip install -r user_manager/requirements.txt
```

Change the file (user_api.py) on line 9 inserting you database information.

Use the file tables_creation.sql to create the database and tables nedded

To start the application, you'll run:

```bash
$ python user_api.py
```

To use the application
======================

Register user
-----------
**Method:** PUT 
**URL:** localhost:5000/user/register
```json
{
	"name":"Clayton",
	"document":"0987654321",
	"email":"clayton@email.com",
	"birth_date":"2021-12-21"
}
```

Retrieve User
-----------
**Method:** GET
**URL:** localhost:5000/user/<id_user>

Retrieve all users
------------------
**Method:** GET
**URL:** localhost:5000/user/0

Change User
-----------
**Method:** POST
**URL:** localhost:5000/user/change
```json
{
	"name":"Clayton RV",
	"document":"0987654321",
	"email":"claytonrv@email.com",
	"birth_date":"2021-12-21"
}
```
Delete User
-----------
**Method:** DELETE
**URL:** localhost:5000/user/delete/<id_user>
