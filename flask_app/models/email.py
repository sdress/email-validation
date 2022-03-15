from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# if many to many or one to many relationship, may need to import other model
# from flask_app.models import model_name

# insert name of schema
db = 'email_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email_add = data['email_add']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # create method
    @classmethod
    def add(cls, data):
        # some query
        query = "INSERT INTO emails (email_add, created_at, updated_at) VALUES ( %(email_add)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)
    
    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(db).query_db(query)
        all_list = []
        for row in results:
            all_list.append( cls(row) )
        return all_list
    
    @classmethod
    def get_last(cls):
        query = "SELECT * FROM emails ORDER BY emails.id DESC LIMIT 1;"
        results = connectToMySQL(db).query_db(query)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE emails SET email_add = %(email_add)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    #basic validation form
    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true
        query = "SELECT * FROM emails WHERE email_add = %(email_add)s"
        results = connectToMySQL(db).query_db(query, email)
        if len(results) >= 1:
            flash("Email address already exists")
            is_valid = False
        if not EMAIL_REGEX.match(email['email_add']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid