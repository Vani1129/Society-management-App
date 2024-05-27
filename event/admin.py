from django.contrib import admin
from .models import Event, Notice

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('Event_name', 'description', 'date')
    
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('society', 'title', 'description', 'posted_date')