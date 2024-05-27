from django.contrib import admin
from .models import Society, Building, Unit

@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'address', 
        'city', 
        'pincode', 
        'state', 
        'country', 
        'type', 
        'registration_number', 
        'total_flats', 
        'contact_email', 
        'contact_phone', 
        'created', 
        'updated'
    )
    search_fields = ('name', 'city', 'state', 'registration_number')
    list_filter = ('state', 'city', 'type')

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'society', 'building')
    list_filter = ('society',)
    search_fields = ('name', 'society__name')
    
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('building', 'unit_number', 'unit_type')