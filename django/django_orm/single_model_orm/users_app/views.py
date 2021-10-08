from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    return render(request,'index.html')

def add_user(request):
    if request.method == 'POST':
        
        return render(request, 'add_user', context)

def results(request):
    return redirect(request, '/')

# Create your views here.
