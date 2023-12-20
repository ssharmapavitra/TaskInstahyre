# users/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Contact, SpamReport
from .serializers import UserProfileSerializer, ContactSerializer, SpamReportSerializer, CreateUserSerializer

class UserProfileCreateView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

class ContactCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        # Associate the contact with the authenticated user
        serializer.save(user=self.request.user.userprofile)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the contact with the same phone number already exists
        phone_number = serializer.validated_data['phone_number']
        existing_contact = Contact.objects.filter(user=self.request.user.userprofile, phone_number=phone_number).first()

        if existing_contact:
            return Response({"detail": "Contact with this phone number already exists for the user."}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ContactListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.userprofile)

class SearchView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('query', '')
        response_data = UserProfile.objects.filter(name__startswith=query).values('name','phone_number') | UserProfile.objects.filter(name__contains=query).values_list('name','phone_number')
        response = Response({'query':query, 'result':response_data})
        return response

class SearchByPhoneView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('query', '')
        response_data = UserProfile.objects.filter(phone_number=query).values('name')
        response = Response({'query':query, 'result':response_data})
        return response

class SpamReportCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SpamReportSerializer
