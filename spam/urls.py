from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpamReportViewSet

router = DefaultRouter()
router.register(r'spam-reports', SpamReportViewSet)

app_name = 'spam'  # Add this line

urlpatterns = [
    path('', include(router.urls)),
]
