from django.shortcuts import render, redirect
import random, pytz
from datetime import datetime
from pytz import timezone

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        
    context = {
        "activities":request.session["activities"]
    }
    return render(request,'index.html', context)

def process_money(request):
    if request.method == 'POST':
        #SETUP
        myGold = request.session['gold']
        activities = request.session['activities']
        location = request.POST['location']
        #MY LOCATION
        if location == 'farm':
            #earn 10-20 gold
            goldThisTurn = round(random.random() * 10 + 10)
        elif location == 'cave':
            #earn 10-20 gold
            goldThisTurn = round(random.random() * 5 + 10)
        elif  location == 'house':
            #earn 10-20 gold
            goldThisTurn = round(random.random() * 3 + 2)
        else:
            #do casino stuff
            winOrLose = round(random.random())
            if winOrLose == 1:
                goldThisTurn = round(random.random() * 50)
            else:
                goldThisTurn = (round(random.random() * 50) * -1)


        #MY TURN STUFF
        date_format='%m/%d.%Y %H:%M:%S %Z'
        date=datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Eastern'))
        myTime = date.strftime(date_format)

        myGold += goldThisTurn
        request.session['gold'] = myGold

        if goldThisTurn >= 0:
            str = f"Earned {goldThisTurn} from the {location}Yay!! {myTime}"
        else:
            goldThisTurn *= -1    
            str = f"Lost {goldThisTurn} from the {location} Dangit!!{myTime}"
        activities.insert(0, str)
        
        request.session['activities'] = activities
    return redirect('/')







# Create your views here.
