# users/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Contact, SpamReport
from .serializers import UserProfileSerializer, ContactSerializer, SpamReportSerializer

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ContactListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.userprofile)

class SearchView(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return UserProfile.objects.filter(name__startswith=query) | UserProfile.objects.filter(name__contains=query)

class SpamReportCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SpamReportSerializer
