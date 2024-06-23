from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class loginUserAPI(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request,'login.html')
    
    def post(self,request):
        if 'login' in request.POST:
            if not request.user.is_authenticated:
                user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
                if user is not None:
                    login(request, user)
                    user_data = UserSerializer(user).data
                    if 'web' in request.POST:
                        return redirect('/')

                    return Response({"data" : user_data, "status" : "success", "message" : "Login Successfully"})
                else:
                    if 'web' in request.POST:
                        messages.success(request, "Invalid Credentials")
                        return redirect('/login')
            else:
                return redirect('/')

        elif 'signup_web' in request.POST:
            #signup code goes here
            pass
        else:
            # other api for login sing up goes here
            pass
            
class logoutUserAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')
        else:
            return redirect('/')
    
   