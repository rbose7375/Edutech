from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from .models import *
from .serializer import *

class SearchProductAPI(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self,request):
        query = request.GET.get('query','')
        if query:
            data = ProductServices.objects.filter(category__name__icontains =query,is_active = True)
            if not data.exists():
                data = ProductServices.objects.filter(name__icontains =query,is_active = True)
            data_serialized = ProductServicesSerializer(data[:10], many = True).data
            context = {
                'status' : 'success',
                'message' : 'data fetched',
                'data' : data_serialized,
                'error' : '000',
            }
            return Response(context, status = status.HTTP_200_OK)
        else:
            context = {
                'status' : 'fail',
                'message' : '"query" parameter missing',
                'data' : '',
                'error' : '001',
            }
            return Response(context, status = status.HTTP_400_BAD_REQUEST)
    
class ProductCategoryAPI(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self,request):
        data = ProductServicesCategory.objects.filter(is_active = True)
        data_serialized = ProductServicesCategorySerializer(data, many = True).data
        context = {
            'status' : 'success',
            'message' : 'data fetched',
            'data' : data_serialized,
            'error' : '000',
        }
        return Response(context, status = status.HTTP_200_OK)
    