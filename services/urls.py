from django.urls import path
from . import views
urlpatterns = [
    path('search', views.SearchProductAPI.as_view(), name='search'),
    path('get-gategories', views.ProductCategoryAPI.as_view(), name='search'),
]
