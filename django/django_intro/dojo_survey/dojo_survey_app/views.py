from django import http
from django.shortcuts import render, redirect, HttpResponse


#def index(request):
#    HttpResponse print('This is a frist page request')
#    return render(request, "index.html")

def results(request):
    if request.method == "GET":
        print('This is a get response')
        return render(request, 'results.html')
    if request.method == "Post":
        print('this is a post method')
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        return redirect('/results')

def index(request):
    print('got here from redirect!')
    return render(request, 'index.html')

# Create your views here.
