from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from django.conf import settings

class Post(models.Model):
  #  user = models.OneToOneField(User)
    Name = models.CharField(max_length=200)
    Email_ID = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    DOB = models.CharField(max_length=30)
    Flag = models.CharField(max_length=1)
    ORG = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

   # def __str__(self):
#	return self.user.username

    def publish(self):
        self.published_data = timezone.now()
        self.Name = 'Thejas'
        self.save()

#def create_profile(sender, **thejas):
#    if thejas['created']:
#        user_profile = UserProfile.objects.create(user=thejas['instance'])

#post_save.connect(create_profile,sender=User)

