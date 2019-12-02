from __future__ import unicode_literals
from django.db import models
from apps.login_app.models import User

class Book_Manager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = "Title cannot be blank"
        elif len(postData['title']) <2:
            errors['message'] = "Title cannot be less than 10 characters"
        if len(postData['description']) == 0:
            errors['description'] = "Description cannot be blank"
        elif len(postData['description']) <3:
            errors['description'] = "Description name cannot be less than 3 characters"    
        return errors

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name="books")
    like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Book_Manager()
    
