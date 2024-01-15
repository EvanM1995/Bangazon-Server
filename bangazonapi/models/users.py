from django.db import models

class Users(models.Model):
    name_first = models.CharField(max_length=25)
    name_last = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
