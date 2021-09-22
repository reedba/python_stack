from django import http
from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, "index.html")

def results(request):
    if request.method == 'POST':
        context = {
            'name':request.POST['name'],
            'location':request.POST['location'],
            'language':request.POST['language'],
            'comment':request.POST['comment']
        }
    return render(request, 'results.html', context)

# Create your views here.
