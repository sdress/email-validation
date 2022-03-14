from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# if many to many or one to many relationship, may need to import other model
# from flask_app.models import model_name

# insert name of schema
db = 'name_of_schema'

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']    

    # create method
    @classmethod
    def create(cls, data):
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
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE emails SET email_add = %(email_add)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    def delete(cls, data):
        query = "DELETE * FROM emails WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    #basic validation form
    @staticmethod
    def validate_survey(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Name is a required field.")
            is_valid = False
        return is_valid