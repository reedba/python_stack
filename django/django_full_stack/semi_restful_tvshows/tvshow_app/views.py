
from django.shortcuts import render, redirect
from .models import Shows
from django.contrib import messages


def index(request):
    context = {
        'shows':Shows.objects.all()
    }
    return render(request, 'add_show.html',context)


def create_show(request):
    if request.method == 'POST':

        errors = Shows.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

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

def view_show(request, show_id):
    show = Shows.objects.get(id = show_id)
    return redirect(f'/show_details/{show.id}')


def remove_show(request, show_id):
    show = Shows.objects.get(id = show_id)
    show.delete()
    return redirect('/shows_list')

def edit_show(request, show_id):
    context = {
        'show':Shows.objects.get(id = show_id)
    }
    return render(request,"edit_show.html", context)


def update_show(request, show_id):
    to_update = Shows.objects.get(id = show_id)
    to_update.title = request.POST['title']
    to_update.description = request.POST['description']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.save()
    return redirect(f'/show_details/{to_update.id}')


# Create your views here.
