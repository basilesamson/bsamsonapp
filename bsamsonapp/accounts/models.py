from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.CharField(default='media/profile_picture/default.png', max_length=100)
    description = models.CharField('Description', blank=True, null=True, max_length=500)
    job = models.CharField('Job', blank=True, null=True, max_length=40)

    def __str__(self):  
        return "{}".format(self.user)