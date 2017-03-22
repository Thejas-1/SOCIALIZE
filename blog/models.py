from django.db import models
from django.utils import timezone


class Post(models.Model):
    Name = models.TextField()
    title = models.CharField(max_length=200)
    mobile = models.TextField()
    DOB = models.TextField()
    Flag = models.CharField(max_length=1)
    ORG = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

