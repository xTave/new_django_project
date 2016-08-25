from django.db import models
from new_django_project.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model


class Branch(models.Model):
    topics = models.ManyToManyField(Topic)


class Topic(models.Model):
    posts = models.ManyToManyField(Post)
    title = models.CharField()


class Post(models.Model):
    author = models.ForeignKey(get_user_model())
    text = models.TextField()
    posted_date = models.TimeField()