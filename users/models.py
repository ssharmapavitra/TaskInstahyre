# users/models.py
from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True)
    phone_number = models.CharField(max_length=10, unique=True)
    email_address = models.EmailField(blank=True, null=True)

class Contact(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)

class SpamReport(models.Model):
    reporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
