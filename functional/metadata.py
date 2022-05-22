import pymysql 

cursor = db = None 

class trvStore:
    def __init__(self):
        self.user = 'root'
        self.password = ''
        self.database = 'trvStore'
        self.host = 'localhost'

    def openDB(self):
        global db, cursor
        db = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
        cursor = db.cursor(pymysql.cursors.DictCursor)

    def closeDB(self):
        global db, cursor 
        db.close()
    
    def insert_enduser(self, data):
        global db, cursor
        self.openDB() 
        cursor.execute(
            f"""
                INSERT INTO register_enduser (
                    email, name, username, password
                ) values (
                    '{data[0]}', '{data[1]}', '{data[2]}','{data[3]}'
                )
            """
        )
        db.commit()
        self.closeDB()
    
    def email_exist(self, email):
        global db, cursor
        self.openDB()
        cursor.execute(
            f"""
                SELECT * FROM register_enduser WHERE email = '{email}'
            """
        )
        fetch = cursor.fetchone()
        return fetch