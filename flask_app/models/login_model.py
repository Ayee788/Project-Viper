from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import pprint
# create Class..pay attention to the capital letter 
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Volunteer:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.email = data['email']
        self.phone = data['phone']
        
    @classmethod
    def save(cls,data):
        query= 'INSERT INTO volunteers (first_name,last_name,email,phone) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(phone)s);'
        result = connectToMySQL(DATABASE).query_db(query,data)
        print('this is the result from the database----->',result)
        return result
    
    @classmethod
    def get_email(cls,data):
        query = 'SELECT * FROM volunteers WHERE email = %(email)s;' 
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:             #this is checking for duplicate email addresses through database  
            return cls(result[0])
        return False
    
    @classmethod
    def get_id(cls,data):
        query = 'SELECT * FROM volunteers WHERE id = %(id)s;' 
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:             #this is checking for duplicate id through database  
            return cls(result[0])
        return []
    
    # @staticmethod
    # def validate_user(data):
    #     is_valid = True
        
    #     if len(data['first_name']) <= 2:
    #         flash('first name field is not valid','register')
    #         is_valid = False
    
    #     if len(data['last_name']) <= 2:
    #         flash('last name field is not valid','register')
    #         is_valid = False
            
    #     if len(data['password']) <= 2:
    #         flash('password field is not valid, please enter a valid password','register')
    #         is_valid = False
        
    #     elif not data['confirm_password'] == data['password']:
    #         flash('password field is not valid, please enter a valid password','register')
    #         is_valid = False
        
    #     if len(data['email']) <= 1:
    #         flash('This is not a valid email', 'register')
    #         is_valid = False
    #         return is_valid
        
    #     elif not EMAIL_REGEX.match(data['email']): 
    #         flash("Invalid email address!",'register')
    #         is_valid = False
    #         return is_valid 
    #     else: 
    #         dict_email = {
    #             'email' : data['email'] 
    #         }
    #     another_user = User.get_email(dict_email)
    #     if another_user: 
    #         is_valid = False
    #         flash('This email is taken please select another email','register')
        
    #     return is_valid
    
    # add a class method to query the database and return all volunteers and their information
    @classmethod
    def get_all_volunteers(cls):
        query = 'SELECT * FROM volunteers;'
        results = connectToMySQL(DATABASE).query_db(query)
        volunteers = []
        for volunteer in results:
            volunteers.append(cls(volunteer))
        return volunteers
    # add a class method to query the database and return one volunteer and their information
    @classmethod
    def get_one_volunteer(cls,data):
        query = 'SELECT * FROM volunteers WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    # add a class method to query the database and update one volunteer and their information
    @classmethod
    def update_volunteer(cls,data):
        query = 'UPDATE volunteers SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, phone = %(phone)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query,data)
    # add a class method to query the database and delete one volunteer and their information
    @classmethod
    def delete_volunteer(cls,data):
        query = 'DELETE FROM volunteers WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query,data)    
    # add more models and controllers as needed