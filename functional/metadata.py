import pymysql 
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='./.env')

cursor = db = None 

class trvStore:
    def __init__(self):
        self.user = os.getenv('NAME')
        self.password = os.getenv('PASSWORD')
        self.database = os.getenv('DATABASE')
        self.host = os.getenv('HOST')

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
    
    def insert_codeV(self, data):
        global db, cursor
        self.openDB() 
        cursor.execute(
            f"""
                INSERT INTO forgetted_password_tokenconfirm (
                    token, created, user_id_id, confirm
                ) values (
                    '{data[0]}', '{data[1]}', '{data[2]}', 'N'
                )
            """
        )
        db.commit()
        self.closeDB()
    
    def search_validation_code(self, token):
        global db, cursor 
        self.openDB()
        cursor.execute(
            f"""
                SELECT * FROM forgetted_password_tokenconfirm WHERE token='{token}'
            """
        )
        fetch = cursor.fetchone()
        return fetch
    
    def update_table_token(self, data):
        global db, cursor
        self.openDB() 
        cursor.execute(
            f"""
                UPDATE 
                    forgetted_password_tokenconfirm 
                SET 
                    confirm='Y', 
                    when_confirm='{data[0]}'
                WHERE 
                    token='{data[1]}'
            """
        )
        db.commit()
        self.closeDB()
    
    def update_password(self, data):
        global db, cursor
        self.openDB() 
        cursor.execute(
            f"""
                UPDATE 
                    register_enduser
                SET  
                    password='{data[0]}'
                WHERE 
                    id='{data[1]}'
            """
        )
        db.commit()
        self.closeDB()