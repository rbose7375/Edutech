from django.contrib import admin
from .models import *


class ProductServicesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','is_active','created_date','update_date']
    search_fields = ['name']
    

admin.site.register(ProductServicesCategory, ProductServicesCategoryAdmin)

class ProductServicesAdmin(admin.ModelAdmin):
    list_display = ['category','name','price','experties_level','is_active']
    search_fields = ['category','name','price']

admin.site.register(ProductServices, ProductServicesAdmin)