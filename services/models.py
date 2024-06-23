from django.db import models
from django_quill.fields import QuillField
import datetime

# Create your models here.

class ProductServicesCategory(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True, default='')
    slug = models.CharField(max_length=1000,null=True, blank=True, default='')
    image = models.FileField(upload_to='category', null=True, blank=True, default='')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'unknown service'
        
class ProductServices(models.Model):
    currency = (('₹','₹'),('$','$'),('€','€'))
    
    category = models.ForeignKey(ProductServicesCategory, related_name='service_category', default=None, null=True, blank=True, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=100,null=True, blank=True, default='')
    price_currency = models.CharField(max_length=100,choices=currency,null=True, blank=True, default='')
    price = models.IntegerField(null=True, blank=True, default=0)
    length = models.CharField(max_length=100,null=True, blank=True, default='')
    experties_level = models.CharField(max_length=100,null=True, blank=True, default='')
    open_time = models.TimeField(datetime.time(10, 0))
    close_time = models.TimeField(datetime.time(18, 0))
    image = models.FileField(upload_to='product', null=True, blank=True, default='')
    description = QuillField(default='', null=True, blank=True)
    slug = models.CharField(max_length=1000,null=True, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'unknown service'