from rest_framework import viewsets
from .models import SpamReport
from .serializers import SpamReportSerializer

class SpamReportViewSet(viewsets.ModelViewSet):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer
