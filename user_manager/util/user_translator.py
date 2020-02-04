from model import UserModel
import datetime

class UserTranslator:

    def translate_row_to_user(self, rows):
        users = []
        for row in rows:
            print(row)
            users.append(UserModel(user_id=row[0], name=row[1], id_document=row[2], email=row[3], birth_date=row[4], register_date=row[5]))
        return users

    def translate_json_to_user(self, json):
        user_id = None
        registration_date = None
        try:
            user_id = json['id']
            registration_date = json['registration_date']        
            print("user update")
        except:
            print("user registration")
        name = json['name']
        document = json['document']
        email = json['email']
        birth_date = datetime.datetime.strptime(json['birth_date'], '%Y-%m-%d')
        
        return UserModel(user_id=user_id, name=name, id_document=document, email=email, birth_date=birth_date, register_date=registration_date)

    def object_dict(self, obj):
        if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
            return obj.__str__()
        else:
            return obj.__dict__