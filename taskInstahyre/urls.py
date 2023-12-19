# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # debug_toolbar
from django.conf.urls.static import static # debug_toolbar
from users.views import UserProfileCreateView, ContactCreateView, ContactListView, SearchView, SpamReportCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserProfileCreateView.as_view(), name='register'),
    path('api/contacts/', ContactListView.as_view(), name='contacts'),
    path('api/add-contact/', ContactCreateView.as_view(), name='add_contact'),
    path('api/search/', SearchView.as_view(), name='search'),
    path('api/report-spam/', SpamReportCreateView.as_view(), name='report_spam'),
    path("__debug__/", include('debug_toolbar.urls')),
]

if not settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # debug_toolbar