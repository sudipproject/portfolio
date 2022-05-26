from django.urls import path
from .import views

urlpatterns = [
    path('profile/',views.employeehome,name="profile")
]