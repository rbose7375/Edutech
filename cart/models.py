from django.db import models
from services.models import ProductServices
from users.models import User


class FavoriteList(models.Model):
    user = models.ForeignKey(User, related_name='user_favorite_list', null=True, blank=True,default=None, on_delete=models.SET_DEFAULT)
    product =  models.ForeignKey(ProductServices, related_name='product_favorite_list', null=True, blank=True,default=None, on_delete=models.SET_DEFAULT)
    is_booked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.user:
            if self.user.first_name:
                return self.user.first_name
            else:
                return 'Unknown user'
        else:
            return 'Unknown user'
            
class BookClass(models.Model):
    user = models.ForeignKey(User, related_name='user_book_class', null=True, blank=True,default=None, on_delete=models.SET_DEFAULT)
    product =  models.ForeignKey(ProductServices, related_name='product_book_class', null=True, blank=True,default=None, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    email = models.CharField(max_length=100, null=True, blank=True, default='')
    phone = models.CharField(max_length=100, null=True, blank=True, default='')
    address = models.CharField(max_length=100, null=True, blank=True, default='')
    payment_method = models.CharField(max_length=100, null=True, blank=True, default='')
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
            
    def __str__(self):
        if self.user:
            if self.user.first_name:
                return self.user.first_name
            else:
                return 'Unknown user'
        else:
            return 'Unknown user'
    

