"""
URL configuration for taskInstahyre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import include
from django.conf import settings # debug_toolbar
from django.conf.urls.static import static # debug_toolbar
from users.views import UserProfileCreateView, ContactListView, SearchView, SpamReportCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserProfileCreateView.as_view(), name='register'),
    path('api/contacts/', ContactListView.as_view(), name='contacts'),
    path('api/search/', SearchView.as_view(), name='search'),
    path('api/report-spam/', SpamReportCreateView.as_view(), name='report_spam'),
    path("__debug__/", include('debug_toolbar.urls')), # debug_toolbar
]

if not settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # debug_toolbar

