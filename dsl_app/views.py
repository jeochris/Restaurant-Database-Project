from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Menu, User, Restaurant, Review, ReviewDetails, Tag

def index(request):
    pass