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

def logout(request):
    request.session.flush()
    return redirect('/')

def main_page(request):
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        'user': this_user[0],
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
        'company':Company.objects.get(id = id),
        'resumes':Resume_Submission.objects.all(),
        
    }
    
    return render(request,'resume_dets.html', context)

def interview_dets(request, id):
    context = {
        'company':Company.objects.get(id = id)
    }
    return render(request,'interview_dets.html', context)

def favorite(request, company_id):
    user = User.objects.get(id=request.session["user_id"])
    company = Company.objects.get(id=company_id)
    user.favorited_company.add(company)

    return redirect('/main_page')

def add_resume_dets(request, id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        resume_details = Resume_Submission.objects.create(job_title = request.POST['position'], location = request.POST['location'], follow_up = request.POST['follow_up'], poster_name = request.POST['contact_name'], date_submitted = request.POST['submitted'], poster_email = request.POST['contact_email'], skills = request.POST['skills'], poster_number = request.POST['contact_phone'], related_company = company)
    return redirect(f'/resume_dets/{id}')

