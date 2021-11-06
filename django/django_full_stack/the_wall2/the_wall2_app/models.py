from django.db import models
import re
import bcrypt 

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name'])<2:
            errors['first_name']= 'First Name must be atleast two characters long'
        if len(postData['last_name'])<2:
            errors['last_name']= 'Last Name must be atleast two characters long'
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email']= 'You must enter an Email'
        elif not email_regex.match(postData['email']):               
            errors['email'] = "Invalid email address!"

        current_users = User.objects.filter(email = postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = 'That email is already in use'

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be atleast 8 characters long'
        if postData['password'] != postData['cf_password']:
            errors['mismatch'] = 'Your passwords do not match'

        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email = postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = 'Email must be entered'
        if len(postData['password']) < 8:
            errors['password'] = 'An 8 character password must me entered'
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['password'] = 'Email and password does not match'


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Wall_Message(models.Model):
    message = models.TextField()
    poster = models.ForeignKey(User, related_name="user_messages", on_delete = models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    comment = models.TextField()
    poster = models.ForeignKey(User, related_name="users_comments", on_delete = models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name='post_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
