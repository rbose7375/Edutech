from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('Staff', 'Staff'),
        ('Student', 'Student'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    email = models.EmailField(_('email address'), null=True, blank=True, default='')
    username = models.CharField(_('username'), null=True, blank=True, default='', max_length=50,unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    registration_number = models.CharField(default='', null=True, blank=True ,max_length=25)
   # country_code = models.CharField(_('Contact phone number'), max_length=13, unique=True)
    mobile = models.CharField(_('Contact phone number'), max_length=13, null=True, blank=True, default=0)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=20, blank=True, choices=GENDER, default='')
    # profile_picture = models.ImageField(upload_to='listings-eyopto', null=True)
    objects = UserManager()
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', default='', null= True, blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', default='', null= True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        if full_name.strip():
            return full_name.strip()
        else:
            return self.username
            

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def is_password_change(self):
        try:
            yes = self.studentdashboard_user.get(user__id = self.id).password_change
            return yes
        except:
            return False
        
    def get_token(self):
        try:
            yes = Token.objects.get(user = self)
            return yes
        except:
            return False
        
    def fav_list(self):
        return self.user_favorite_list.filter(is_active=True).values_list('id', flat=True)

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if not Token.objects.filter(user=instance).exists():
        Token.objects.create(user=instance)
