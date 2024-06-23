from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'username', 'email' ]
    list_display = ['username','email','first_name','is_active','is_staff', 'date_joined']

admin.site.register(User, UserAdmin)