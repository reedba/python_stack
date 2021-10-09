from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
            'all_users':User.objects.all()
        }
    return render(request,'index.html', context)

def add_user(request):
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], e_mail=request.POST['e_mail'], age=request.POST['age'])
        return redirect('/')


# Create your views here.

#Make sure Im using redirect correctly?
#Am I using Context and how to get it to link to HTML?
#Is session only to check if things work?
#How to get the ID to show up in the table?
