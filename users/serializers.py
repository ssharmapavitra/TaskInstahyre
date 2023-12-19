# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Contact, SpamReport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone_number', 'email_address')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        # Use phone_number as the username
        user_data['username'] = validated_data['phone_number']
        user = User.objects.create_user(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile

    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'user', 'name', 'phone_number')

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ('id', 'reporter', 'phone_number')
