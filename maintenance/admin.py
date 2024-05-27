from django.contrib import admin
from .models import Maintenance

# Register your models here.
@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('unit', 'user', 'description', 'status')