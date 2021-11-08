from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])

    context ={
        'comments':Comment.objects.all(),
        'messages':Wall_Message.objects.all(),
        'user':User.objects.all(),
        'user1': this_user[0]
    }
    return render(request,'the_wall.html', context)


def log_reg(request):
    request.session.flush()
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login_registration')
        #hash the password
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        #create a user
        new_user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email =    request.POST['email'], password = hashed_pw)
        #create a session
        request.session['user_id'] = new_user.id
        return redirect('/')
    return redirect('login_registration')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        'user': this_user[0],
        'messages':Wall_Message.objects.all()

    }

    return render(request, 'the_wall.html', context)

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login_registration')
        this_user = User.objects.filter(email = request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/')
    return redirect ('/login_registration')

def logout(request):
    request.session.flush()
    return redirect('/login_registration')

def create_message(request):
    if request.method == 'POST':
        wall_message = Wall_Message.objects.create(message=request.POST['message'], poster = User.objects.get(id = request.session['user_id']))
    return redirect('/success')