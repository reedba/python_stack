from django.shortcuts import render, HttpResponse 

def index(request):
    print('Hello World')
    return HttpResponse('placeholder to display a list of all blogs')


def new(request):
    print('new request')
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    print('created a page')
    return HttpResponse('placeholder to display a creating a blog')



def show(request, my_val):
    print(my_val)
    return HttpResponse(f'placeholder to display blog {my_val}')

def edit(request, my_val):
    print(my_val)
    return HttpResponse(f'placeholder to edit blog {my_val}')

def destroy(request, my_val):
    print('destroyed')
    return HttpResponse(f'destroyed blog {my_val}')


# Create your views here.
