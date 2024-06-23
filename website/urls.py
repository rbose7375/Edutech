from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexPage,name='index'),
    path('all-classes', views.allClass,name='allClass'),
    path('all-classes/<str:slug>', views.allCourseSingleCategory,name='allCourseSingleCategory'),
    path('class/<str:slug>', views.singleCourse,name='singleCourse'),
    path('book/<str:slug>', views.bookCourse,name='bookCourse'),
    path('thank-you', views.thankYou,name='thankYou'),
    path('favorite-list', views.favoriteList,name='thankYou'),
]
