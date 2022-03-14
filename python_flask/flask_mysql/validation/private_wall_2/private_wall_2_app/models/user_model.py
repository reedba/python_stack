from private_wall_2_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash


# validator for the email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    # Sets a variable for my database
    db_name = 'private_wall_schema'
    # Initializes the database user model with all fields 
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #Sets a class method for saving the user data upon registering
    @classmethod
    def save(cls,data):
        # querys the databasae and save the data to the Database
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        # Get all the users in the database
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        #creates an empty list to append the users data into
        users = []
        #iterates through each row in the results and then appends into tyhe new list so we can return it to the controllers file
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        # This query will get all the data by the email passed through the method
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        # if there is no data it will return false
        if len(results) < 1:
            return False
        return cls(results[0])# then this will return the class instance at the 1st position

    @classmethod
    def get_by_id(cls,data):# gets the user data by the id
        query = "SELECT * FROM users WHERE id = %(id)s;" # querys the data by the id
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid= False
        if user['password'] != user['cf_password']:
            flash("Passwords don't match")
        return is_valid