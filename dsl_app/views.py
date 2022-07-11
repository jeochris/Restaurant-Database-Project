from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from dsl_app.forms import UserForm
from django.utils import timezone

def index(request): # main page
    return render(request, 'dsl_app/main.html')