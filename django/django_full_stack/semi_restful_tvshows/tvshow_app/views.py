
from django.shortcuts import render, redirect
from .models import Shows


def index(request):
    context = {
        'shows':Shows.objects.all()
    }
    return render(request, 'add_show.html',context)


def create_show(request):
    if request.method == 'POST':
        tv_show = Shows.objects.create(title=request.POST['title'],description=request.POST['description'],release_date=request.POST['release_date'],network=request.POST['network'])
        
    return redirect(f'/show_details/{tv_show.id}')


def shows_list(request):
    context= {
        'shows':Shows.objects.all()
    }
    return render(request,'shows_list.html',context)


def show_details(request, show_id):
    context ={
        'show':Shows.objects.get(id = show_id),
        'shows':Shows.objects.all()

    }
    return render(request,'tv_show_dets.html',context)


def edit_show(request):
    return render(request,'edit_show.html')


# Create your views here.
