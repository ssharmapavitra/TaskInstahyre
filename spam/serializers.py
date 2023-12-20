from rest_framework import serializers
from .models import SpamReport

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ['id', 'reporter', 'reported_number', 'created_at']
