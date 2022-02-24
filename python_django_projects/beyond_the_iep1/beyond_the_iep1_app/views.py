from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teacher_form(request):
    return render(request, 'teacher_form.html')