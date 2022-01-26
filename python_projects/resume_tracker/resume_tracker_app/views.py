from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

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
    return redirect('/main_page')

def login(request):
    if request.method == 'POST':
        errors = User.objects.Login_Validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/')
        request.session['user_id'] = User.objects.filter(email = request.POST['log_email'])[0].id
    return redirect ('/main_page')

def main_page(request):
    context = {
        'this_user':User.objects.get(id = request.session['user_id']),
        'companies':Company.objects.all()
    }
    return render(request,'main_page.html',context)

def add_company(request):
    current_user = User.objects.get(id=request.session["user_id"])
    if request.method == 'POST':
        company_dets = Company.objects.create(company = request.POST['company_dets'], website = request.POST['website'], creator = current_user)
    return redirect('/main_page')

def resume_dets(request, id):
    context = {
        'company':Company.objects.get(id = id)
    }
    return render(request,'resume_dets.html', context)
