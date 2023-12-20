from django.contrib import admin
from .models import UserProfile, Contact, SpamReport

admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(SpamReport)