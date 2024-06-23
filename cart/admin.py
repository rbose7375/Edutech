from django.contrib import admin
from .models import *


class FavoriteListAdmin(admin.ModelAdmin):
    list_display = ['user','product','is_booked','is_active','created_date']
    search_fields = ['user','product']
admin.site.register(FavoriteList, FavoriteListAdmin)

class BookClassAdmin(admin.ModelAdmin):
    list_display = ['user','product','is_paid','is_active','created_date']
    search_fields = ['user','product']
admin.site.register(BookClass, BookClassAdmin)