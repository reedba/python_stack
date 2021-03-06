from django.db import models
import re
import bcrypt


# Create your models here.

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['existingUser'] = 'User already registered with that username'
        if len(postData['first_name']) < 2:
            errors['first_name']='First Name should be atleast 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name']='Last Name should be atleast 2 characters'
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors['first_name']='Password should be atleast 8 characters'
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw']='Password and confirm password must match'
        return errors
    
    def Login_Validator(self, postData):
        errors = {}
        checkUser = User.objects.filter(email = postData['log_email'])
        if len(checkUser) < 1:
            errors['NoUser'] = 'Invalid Username and Password cobination'
        elif not bcrypt.checkpw(postData['log_password'].encode(), checkUser[0].password.encode()):
            errors['passwordNoMatch'] = 'Invalid user and password combination'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
