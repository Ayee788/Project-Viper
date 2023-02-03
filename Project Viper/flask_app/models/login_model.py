from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import pprint
# create Class..pay attention to the capital letter 
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.email = data['email']
        self.password = data['password']
        
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users(first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);'
        result = connectToMySQL(DATABASE).query_db(query,data)
        print('this is the result from the database----->',result)
        return result
    
    @classmethod
    def get_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;' 
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:             #this is checking for duplicate email addresses through database  
            return cls(result[0])
        return False
    
    @classmethod
    def get_id(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s;' 
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:             #this is checking for duplicate id through database  
            return cls(result[0])
        return []
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        
        if len(data['first_name']) <= 2:
            flash('first name field is not valid','register')
            is_valid = False
    
        if len(data['last_name']) <= 2:
            flash('last name field is not valid','register')
            is_valid = False
            
        if len(data['password']) <= 2:
            flash('password field is not valid, please enter a valid password','register')
            is_valid = False
        
        elif not data['confirm_password'] == data['password']:
            flash('password field is not valid, please enter a valid password','register')
            is_valid = False
        
        if len(data['email']) <= 1:
            flash('This is not a valid email', 'register')
            is_valid = False
            return is_valid
        
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!",'register')
            is_valid = False
            return is_valid 
        else: 
            dict_email = {
                'email' : data['email'] 
            }
        another_user = User.get_email(dict_email)
        if another_user: 
            is_valid = False
            flash('This email is taken please select another email','register')
        
        return is_valid