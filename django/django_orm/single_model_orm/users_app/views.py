from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('this works')

# Create your views here.
