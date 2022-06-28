from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Menu, User, Restaurant, Review, ReviewDetails, Tag
from django.utils import timezone

def index(request):
    return redirect('/register')

@csrf_exempt
def register(request):
    if request.method == 'GET':
        print('check')
        return render(request, 'dsl_app/register.html')
    
    elif request.method == 'POST':
        new_name = request.POST['name']
        new_id = request.POST['id']
        new_passwd = request.POST['passwd']
        new_person = User(name = new_name, login_id = new_id, login_pw = new_passwd, join_date = timezone.now())
        new_person.save()
        return HttpResponse('User Added')