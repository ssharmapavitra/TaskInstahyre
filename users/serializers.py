# users/serializers.py

from rest_framework import serializers
from .models import UserProfile, Contact, SpamReport

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone_number', 'email_address')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'user', 'name', 'phone_number')

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ('id', 'reporter', 'phone_number')
