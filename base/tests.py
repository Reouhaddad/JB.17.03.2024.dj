from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.index),
    path('login/', TokenObtainPairView.as_view()),
]
