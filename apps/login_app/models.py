#Login View methods
from __future__ import unicode_literals
from django.db import models
import re
nameregex=re.compile(r'^[a-zA-Z]+$')
emailregex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')


class User_Manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        database_emails = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) == 0:
            errors['first_name'] = "First name cannot be blank."
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 letters."
        if not nameregex.match(postData['first_name']):
            errors['first_name'] = "First name must contain letters only."
        if len(postData['last_name']) == 0:
            errors['first_name'] = "Last name cannot be blank"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 letters."
        if not nameregex.match(postData['last_name']):
            errors['last_name'] = "Last name must contain letters only."
        if len(database_emails ) > 0:
                errors['email'] = 'That email exists in the database already.'
        if not emailregex.match(postData['email']):
            errors['email'] = "invalid email"
        if len(postData['password']) < 8:
            errors['password']= "Password must be at least 8 char"
        if str(postData['confirm_password']) !=  str(postData['password']) :
            errors['confirm_password']= "Doesnt match password"
        return errors
    def basic_login(self, postData):
        errors = {} 
        user = User.objects.filter(email=postData['email'])
        if len(postData['password']) == 0:
            errors['password'] = "Please enter password"
        if len(postData['email']) == 0:
            errors['email'] = "Please enter email"
        elif len(user) == 0:
            errors['email'] = "Email does not exist, Please register"
        else:
            user = User.objects.get(email=postData['email'])
            if user.password != postData["password"]:
                errors['password'] = "Password does not match."
        return errors

    def edit_validator(self, postData):
        errors = {}
        if len(postData['description']) == 0:
            errors['description'] = "Description name cannot be blank."
        if len(postData['description']) < 2:
            errors["description"] = "Description should be at least 2 letters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    confirm_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_Manager() 

 
