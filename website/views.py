from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services.models import *
from cart.models import *

def indexPage(request):
    class_categories = ProductServicesCategory.objects.filter(is_active = True)
    classes = ProductServices.objects.filter(is_active = True, is_home = True)
    context =  {
        'categeries' : class_categories,
        'classes' : classes,
    }
    return render(request, 'index.html',context)

def allClass(request):
    class_categories = ProductServicesCategory.objects.filter(is_active = True)
    context =  {
        'categeries' : class_categories,
    }
    return render(request, 'all_classes.html',context)

def allCourseSingleCategory(request, slug):
    class_categories = ProductServices.objects.filter(category__slug = slug)
    context =  {
        'services' : class_categories,
        'prodcut' : True
    }
    return render(request, 'all_classes.html',context)

def singleCourse(request, slug):
    course = ProductServices.objects.get(slug = slug)
    context =  {
        'product' : course,
    }
    return render(request, 'single_class.html',context)

@login_required(login_url='/login')
def bookCourse(request, slug):
    course = ProductServices.objects.get(slug = slug)
    context =  {
        'product' : course,
    }
    return render(request, 'book_order.html',context)

@login_required(login_url='/login')
def favoriteList(request):
    fave_list = FavoriteList.objects.filter(user = request.user, is_active = True)
    context =  {
        'fave_list' : fave_list,
    }
    return render(request, 'fav_list.html',context)

def thankYou(request):
    return render(request, 'thank.html')

def error_404_view(request, exception):
    return render(request, '404.html')
