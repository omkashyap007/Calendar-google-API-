from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login 

def HomePage(request , *args , **kwargs ) :
    context = {}
    return render(request , "home/homePage.html" , context) 

def LoginView(request) : 
    user = User.objects.get(email = "omkashyapcric@gmail.com")
    login(request , user )
    return redirect("")