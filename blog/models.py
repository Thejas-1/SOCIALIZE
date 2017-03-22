from django.db import models
from django.utils import timezone


class Post(models.Model):
    Name = models.CharField(max_length=200)
    Email_ID = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    DOB = models.CharField(max_length=30)
    Flag = models.CharField(max_length=1)
    ORG = models.CharField(max_length=200)

