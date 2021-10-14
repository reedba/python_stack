from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.

def index(request):
    context = {
        'dojos':Dojo.objects.all(),
        'ninja':Ninja.objects.all()
    }
    return render(request,'index.html',context)

def add_dojo(request):
    if request.method == 'POST':
        Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    return redirect('/')

def add_ninja(request):
    if request.method == 'POST':
        Ninja.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],dojo=request.POST['dojo'])
    return redirect('/')
    
