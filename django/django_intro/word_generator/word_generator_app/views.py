from django.shortcuts import render, HttpResponse
import random

def index(request):
    return render(request,'index.html')

# Create your views here.
