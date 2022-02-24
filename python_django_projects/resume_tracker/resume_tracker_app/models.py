from email.policy import default
from typing import ItemsView
from django.db import models
import re
from django import forms

from django.db.models.fields.related import ManyToManyField 
import bcrypt 

# Create your models here.
class UserManager(models.Manager):
    def Validate_Registration(self, postData):
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
        if postData['password'] != postData['cf_password']:
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
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Company(models.Model):
    company = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    user_favorite = models.ManyToManyField(User, related_name='favorited_company')
    creator = models.ForeignKey(User, related_name="company_creator", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Resume_Submission(models.Model):
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_submitted = models.DateTimeField(null=True)
    follow_up = models.DateTimeField(null=True)
    poster_name = models.CharField(max_length=255)
    poster_email = models.CharField(max_length=255)
    poster_number = models.CharField(max_length=255)
    skills = models.TextField()
    user_resumes = models.ForeignKey(User, related_name= "resume_user", on_delete=models.CASCADE)
    related_company = models.ForeignKey(Company, related_name="company_connection", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Interview_Details(models.Model):
    interviewer_name = models.CharField(max_length=255)
    interviewer_email = models.CharField(max_length=255)
    interviewer_phone = models.CharField(max_length=255)
    interview_date = models.DateTimeField()
    questions_asked = models.TextField()
    questions_to_ask = models.TextField()
    interview_follow_up = models.DateTimeField()
    related_resume = models.ForeignKey(Resume_Submission, related_name= "resume_connection", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




