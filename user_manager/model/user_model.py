from datetime import datetime

class UserModel():
    def __init__(self, user_id=None, name=None, id_document=None, email=None, birth_date=None, register_date=None):
        self.id = user_id
        self.name = name
        self.document = id_document
        self.email = email
        self.birth_date = birth_date
        self.registration_date = register_date