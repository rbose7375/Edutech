from django.urls import path
from . import views
urlpatterns = [
    path('login', views.loginUserAPI.as_view(), name='custom_login'),
    path('logout', views.logoutUserAPI.as_view(), name='user_logout')
]
