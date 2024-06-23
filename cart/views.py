from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from services.models import ProductServices
from .models import *
from .serializer import *

class AddFavoriteListAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication = [authentication.TokenAuthentication]
    def get(self, request):
        all_fave_list = FavoriteList.objects.filter(user = request.user, is_active = True)
        context = {
        'status' : 'success',
        'message' : "Data fetched",
        'data' : FavoriteListSerializer(all_fave_list, many = True).data,
        'error' : '000',
        }
        return Response(context, status = status.HTTP_200_OK)
        
        
    def post(self,request):
        product_id = request.POST.get('service_id')
        context = {
        'status' : 'success',
        'message' : "Class marked as favorite",
        'data' : '',
        'error' : '000',
        }
        if product_id:
            product = ProductServices.objects.filter(id = product_id, is_active = True)
            if product.exists():
                favo_item = FavoriteList.objects.filter(user = request.user, product = product.first())
                if favo_item.exists():
                    favo_item = favo_item.first()
                    if favo_item.is_active:
                        favo_item.is_active = False
                        favo_item.save()
                    else:
                        favo_item.is_active = True
                        favo_item.save()
                else:
                    FavoriteList.objects.create(user = request.user, product = product.first())
                return Response(context, status = status.HTTP_200_OK)
            else:
                context['status'] = 'fail'
                context['message'] = "Product inactive / doesn't exist"
                context['error'] = '002'
                return Response(context, status = status.HTTP_400_BAD_REQUEST)
        else:
            context['status'] = 'fail'
            context['message'] = '"service_id" parameter missing'
            context['error'] = '001'
            return Response(context, status = status.HTTP_400_BAD_REQUEST)
    

class BookSerivceAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication = [authentication.TokenAuthentication,authentication.SessionAuthentication]
    
    def get(self, request):
        all_order_service = BookClass.objects.filter(user = request.user, is_active = True)
        context = {
        'status' : 'success',
        'message' : "data fetched",
        'data' : BookClassSerializer(all_order_service, many = True).data,
        'error' : '000',
        }
        return Response(context, status = status.HTTP_200_OK)
    
    def post(self, request):
        product_id = request.POST.get('service_id')
        context = {
        'status' : 'success',
        'message' : "Class marked as favorite",
        'data' : '',
        'error' : '000',
        }
        if product_id:
            product = ProductServices.objects.filter(id = product_id, is_active = True)
            if product.exists():
                book_order = BookClass.objects.create(user=request.user,product=product.first())
                book_order.name=request.POST.get('name')
                book_order.email=request.POST.get('email')
                book_order.phone=request.POST.get('phone')
                book_order.address=request.POST.get('address')
                book_order.payment_method=request.POST.get('payment_method')
                book_order.save()
                favo_item = FavoriteList.objects.filter(user = request.user, product = product.first())
                if favo_item.exists():
                    favo_item = favo_item.first()
                    favo_item.is_booked = True
                    favo_item.save()
                context['data'] = BookClassSerializer(book_order).data
                context['message'] = 'Your class has been booked successfully'
                if 'web' in request.POST:
                    return redirect('/thank-you')
                return Response(context, status = status.HTTP_200_OK)
            else:
                context['status'] = 'fail'
                context['message'] = "Product inactive / doesn't exist"
                context['error'] = '002'
                return Response(context, status = status.HTTP_400_BAD_REQUEST)
        else:
            context['status'] = 'fail'
            context['message'] = '"service_id" parameter missing'
            context['error'] = '001'
            return Response(context, status = status.HTTP_400_BAD_REQUEST)
        