# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Contact, SpamReport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('user','name','phone_number', 'email_address')

class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email_address = serializers.EmailField(required=False)
    
    def create(self, validated_data):
        name = validated_data.get('name')
        phone_number = validated_data.get('phone_number')
        password = validated_data.get('password')
        email_address = validated_data.get('email_address')

        existing_user = User.objects.filter(userprofile__phone_number=phone_number).first()

        if existing_user:
            raise serializers.ValidationError('User with this phone number already exists.')
        
        user = User.objects.create_user(username=name, password=password)

        user_profile = UserProfile.objects.create(user=user, name=name, phone_number=phone_number, email_address=email_address)
        return user_profile
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'user', 'name', 'phone_number')

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ('id', 'reporter', 'phone_number')
