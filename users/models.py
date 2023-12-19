# users/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    email_address = models.EmailField(blank=True, null=True)

class Contact(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

class SpamReport(models.Model):
    reporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
