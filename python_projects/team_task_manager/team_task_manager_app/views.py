from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def register(request):
    if request.method == 'POST':
        errors = User.objects.Validate_Registration(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        #hash the password
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        #create a user
        new_user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email =    request.POST['email'], password = hashed_pw)
        #create a session
        request.session['user_id'] = new_user.id
        return redirect('/')
    return redirect('/create_task')


def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/')
        request.session['user_id'] = User.objects.filter(email = request.POST['log_email'])[0].id
    return redirect ('/create_task')

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'index.html')

def create_task(request):
    return render(request, 'create_task.html')

def edit_task(request):
    return render(request, 'edit_task.html')

def all_tasks(request):
    return render(request,'all_tasks.html')

def complete_task(request):
    return render(request,'complete_task.html')

def view_task(request):
    return render(request, 'view_task.html')