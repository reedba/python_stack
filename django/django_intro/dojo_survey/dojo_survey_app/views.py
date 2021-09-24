from django import http
from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")

#def results(request):
#    if request.method == 'POST':
#        context = {
#        'name':request.POST['name'],
#        'location':request.POST['location'],
#        'language':request.POST['language'],
#        'comment':request.POST['comment']
#        }
#    return render(request, 'results.html', context)


def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/results')

def results(request):
    return render(request, 'results.html')


    

# Create your views here.
