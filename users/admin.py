from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name' ,
                    'email', 
                    'phone',
                    'profile_pic',
                    'otp_code')
    readonly_fields = ('last_login' , 'date_joined', 'created', 'updated')
