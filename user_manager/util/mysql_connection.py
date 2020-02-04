import mysql.connector

class MySQLConnector():

    def __init__(self, host=None, database=None, port=None, user=None, password=None):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.con = None
        self.cursor = None

    def connect(self):
        try:
            self.con = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database, port=self.port)
            return "Connected"
        except Exception as e: print(e)

    def close_connection(self):
        self.con.close()