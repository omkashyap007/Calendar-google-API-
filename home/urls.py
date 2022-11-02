from django.urls import path 
from home import views as home_views

urlpatterns = [
    path("" , home_views.HomePage , name = "site-home") , 
    path("login/" , home_views.LoginView , name = "login-page") , 
]