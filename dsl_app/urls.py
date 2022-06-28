from django.contrib import admin
from django.urls import path, include
from dsl_app import views

urlpatterns = [
    path('', views.index),
    path('register', views.register)
]