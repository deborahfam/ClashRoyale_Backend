from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, default='', unique=TRUE)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default='')