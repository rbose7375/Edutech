from django.urls import path
from . import views
urlpatterns = [
    path('interest-list', views.AddFavoriteListAPI.as_view(), name='favorite_api'),
    path('book-class', views.BookSerivceAPI.as_view(), name='book_class_api'),
]
