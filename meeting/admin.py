from django.contrib import admin
from meeting.models import Meeting, TypeStatus

# Register your models here.
admin.site.register((Meeting, TypeStatus))
