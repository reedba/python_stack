from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display list of blogs")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}.')

def edit(request, number):
    return HttpResponse(f'placeholder to edit blog number:{number}')

def destroy(request, number):
    return redirect('/')


# Create your views here.
