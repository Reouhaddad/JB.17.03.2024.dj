from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.index),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('products/<int:id>', views.ProductView.as_view()),
    path('register/', views.register),
]
