from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True, default=date.today)
    profile_pic = models.ImageField()
    