from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="register-user"),
    path('login/', views.loginUser, name="login-user"),
    path('logout/', views.logout, name="signout-user"),
    
    path('homepage', views.homepage, name="homepage")
]