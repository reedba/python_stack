from django.shortcuts import render, redirect

# Create your views here.


def render(request):
    return render(request, 'log_reg.html')