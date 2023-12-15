from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True, default=date.today)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.user.username
