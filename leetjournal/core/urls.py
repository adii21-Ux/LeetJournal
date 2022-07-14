from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('homepage/', views.homepageView, name="homepage"),
    path('solutions/', views.getUserSolutions, name="user-solutions")
]