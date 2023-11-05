from django.contrib import admin
from .models import Notification, ScheduledEmail
# Register your models here.

admin.site.register(Notification)
admin.site.register(ScheduledEmail)
