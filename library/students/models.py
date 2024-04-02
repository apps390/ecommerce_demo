from django.db import models
from django.contrib.auth.models import AbstractUser


class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    place = models.CharField(max_length=10)


class details(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)


class CustomUser(AbstractUser):
    phone = models.IntegerField(default=0)
    address = models.TextField(default="")

    def __str__(self):
        return self.username
