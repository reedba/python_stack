from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_game(request):
    if request.method == 'GET':
        return render(request, 'details.html')
    if request.method == 'POST':
        print(request.POST)
        request.session['title'] = request.POST['title']
        request.session['company'] = request.POST['company']
        request.session['system'] = request.POST['system']
        request.session['rating'] = request.POST['rating']
        #context = {
        #    'title':request.POST['title'],
        #    'company':request.POST['company'],
        #    'system':request.POST['system'],
        #    'rating':request.POST['rating']
        #}
    return redirect('/game')

#def details_page(request):
#
#    return render(request, 'details.html')
