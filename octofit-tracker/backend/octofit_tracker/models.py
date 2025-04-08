from django.db import models
from djongo import models as djongo_models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    # ...other fields...

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    # ...other fields...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    # ...other fields...

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    # ...other fields...

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ...other fields...
