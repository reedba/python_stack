from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'register.html')

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
        new_user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'], password = hashed_pw)
        #create a session
        request.session['user_id'] = new_user.id
        return redirect('/login_page')
    return redirect('/login_page')

def login_page(request):
    return render(request, 'login_page.html')

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
    if 'q' in request.GET:
        q = request.GET['q']
        company = Company.objects.filter(company__icontains=q)
    else:
        company = Company.objects.all()
    context = {
        'user': this_user[0],
        'this_user':User.objects.get(id = request.session['user_id']),
        'companies':company,
        'resume_count':Resume_Submission.objects.filter(user_resumes = request.session['user_id'])
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
        'resume':Resume_Submission.objects.get(id=id),
        'interviews':Interview_Details.objects.all()
        
    }
    return render(request,'interview_dets.html', context)

def favorite(request, company_id):
    user = User.objects.get(id=request.session["user_id"])
    company = Company.objects.get(id=company_id)
    user.favorited_company.add(company)

    return redirect('/main_page')

def add_resume_dets(request, id):
    company = Company.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])
    if request.method == 'POST':
        resume_details = Resume_Submission.objects.create(job_title = request.POST['position'], location = request.POST['location'], follow_up = request.POST['follow_up'], poster_name = request.POST['contact_name'], date_submitted = request.POST['submitted'], poster_email = request.POST['contact_email'], skills = request.POST['skills'], poster_number = request.POST['contact_phone'], related_company = company, user_resumes = user)
    return redirect(f'/resume_dets/{id}')

def add_interview_dets(request, id):
    resume = Resume_Submission.objects.get(id=id)
    if request.method == 'POST':
        interview_details = Interview_Details.objects.create(interviewer_name = request.POST['interviewer_name'], interviewer_email = request.POST['interviewer_email'], interviewer_phone = request.POST['interviewer_phone'], interview_date = request.POST['interview_date'], questions_asked = request.POST['questions_asked'], questions_to_ask = request.POST['questions_to_ask'], interview_follow_up = request.POST['interview_follow_up'], related_resume = resume)
    return redirect(f'/interview_dets/{id}' )

def delete_resume(request, id):
        destroyed = Resume_Submission.objects.get(id=id)
        destroyed.delete()
        return redirect('/main_page')

def edit_resume_dets(request, id):
    resume = Resume_Submission.objects.get(id=id)
    context = {
        'resume':resume
    }
    return render(request, 'edit_resume_dets.html', context)

def cancel(request):
    return redirect('/main_page')

def update_resume_dets(request, id):
    edit_resume = Resume_Submission.objects.get(id=id)

    edit_resume.job_title = request.POST['update_job_title']
    edit_resume.location = request.POST['update_location']
    edit_resume.date_submitted = request.POST['update_date_submitted']
    edit_resume.follow_up = request.POST['update_follow_up']
    edit_resume.poster_name = request.POST['update_poster_name']
    edit_resume.poster_email = request.POST['update_poster_email']
    edit_resume.poster_number = request.POST['update_poster_number']
    edit_resume.skills = request.POST['update_skills']
    edit_resume.save()
    return redirect('/main_page')


def edit_interview_dets(request, id):
    interview = Interview_Details.objects.get(id=id)
    context = {
        'interview':interview
    }
    return render(request, 'edit_interview_dets.html', context)


def update_interview_dets(request, id):
    edit_interview = Interview_Details.objects.get(id=id)
    edit_interview.interviewer_name = request.POST['update_interviewer_name']
    edit_interview.interviewer_email = request.POST['update_interviewer_email']
    edit_interview.interviewwer_phone = request.POST['update_interviewer_phone']
    edit_interview.interview_date = request.POST['update_interview_date']
    edit_interview.questions_asked = request.POST['update_questions_asked']
    edit_interview.questions_to_ask = request.POST['update_questions_to_ask']
    edit_interview.interview_follow_up = request.POST['update_interview_follow_up']
    edit_interview.save()
    return redirect('/main_page')
    

def favorites(request):
    this_user = User.objects.filter(id = request.session['user_id'])
    company = Company.objects.all()
    context = {
        'user': this_user[0],
        'this_user':User.objects.get(id = request.session['user_id']),
        'companies':company,
        'resume_count':Resume_Submission.objects.filter(user_resumes = request.session['user_id'])
    }
    return render(request,'favorites.html',context)