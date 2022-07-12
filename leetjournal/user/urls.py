from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.registerUser, name="register-user"),
    path('login/', views.loginUser, name="loginuser"),
    path('logout/', views.logout, name="signout-user"),
]