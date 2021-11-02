from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt  

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash,)

    request.session['logged_in_user']= user.id #logs them in
    return redirect('/welcome')


def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    request.session['logged_in_user']= User.objects.filter(email = request.POST['log_email'])[0].id
    print(request.session['logged_in_user'])
    return redirect('/welcome')

def welcome(request):
    return render(request, 'welcome.html')