from model import UserModel
from util import UserTranslator

class UserDataHandler:
    def __init__(self, db_connection=None):
        self.db_conn = db_connection
        self.translator = UserTranslator()

    def register_user(self, user):
        try:
            cursor = self.db_conn.cursor()
            query, query_data = self.create_user_registration_query(user)
            cursor.execute(query, query_data)
            user = cursor.lastrowid
            self.db_conn.commit()
            cursor.close()
            return user
        except:
            return None

    def retrieve(self, user_id):
        if(user_id is not None and int(user_id) > 0):
            query, query_data = self.create_get_user_query(user_id)
        else:
            query, query_data = self.create_list_users_query()
        try:
            cursor = self.db_conn.cursor()
            if query_data:
                cursor.execute(query, query_data)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            users = self.translator.translate_row_to_user(rows)
            self.db_conn.commit()
            cursor.close()
            return users
        except:
            return None

    def update_user(self, user):
        try:
            cursor = self.db_conn.cursor()
            query, query_data = self.create_user_update_query(user)
            print(query, query_data)
            cursor.execute(query, query_data)
            user = cursor.rowcount
            self.db_conn.commit()
            cursor.close()
            return user
        except:
            return None

    def delete(self, user_id):
        try:
            query, query_data = self.create_remove_user_query(user_id)
            cursor = self.db_conn.cursor()
            cursor.execute(query, query_data)
            self.db_conn.commit()
            cursor.close()
            return True
        except:
            return False

    def create_user_registration_query(self, user):
        query = "INSERT INTO USER(name, id_document, email, birth_date) values (%s, %s, %s, %s)"
        query_data = (user.name, user.document, user.email, user.birth_date)
        return query, query_data

    def create_list_users_query(self):
        query = "SELECT * FROM USER ORDER BY ID DESC"
        return query, None

    def create_get_user_query(self, user_id):
        query = "SELECT * FROM USER WHERE id = %s;"
        query_data = (user_id,)
        return query, query_data

    def create_user_update_query(self, user):
        query = "UPDATE USER SET name=%s, id_document=%s, email=%s, birth_date=%s WHERE id=%s"
        query_data = (user.name, user.document, user.email, user.birth_date, user.id)
        return query, query_data

    def create_remove_user_query(self, user_id):
        query = "DELETE FROM USER WHERE id = %s"
        query_data = (user_id,)
        return query, query_data

    def translate_user_rows(self, rows):
        return self.translator.translate_row_to_user(rows)