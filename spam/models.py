from django.db import models
from users.models import User

class SpamReport(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_number = models.CharField(max_length=15)
