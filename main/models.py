from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    comments = models.TextField()
    user = models.ForeignKey(User)

class Message(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    comments = models.ForeignKey(Comment)
    user = models.ForeignKey(User)