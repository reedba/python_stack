from django.shortcuts import render, redirect
from pytz import timezone
import random, pytz
from datetime import datetime

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request,'index.html')

def process_money(request):
    if request.method == 'POST':
        myGold = request.session['gold']
        activities = request.session['activities']
        location = request.POST['location']

        if location == 'farm':
            #earn 10-20 gold
            goldThisTurn = round(random.random() * 10 + 10)
            #add goldthisturn to mygold
            myGold += goldThisTurn
            request.session['gold'] = myGold
            #create date
            date_format='%m/%d.%Y %H:%M:%S %Z'
            #setting time to now and TimeZone to UTC
            date = date.astimezone(timezone('US/Pacific'))
            #setting TZ to US PACIFIC('US/Pacific))
            #displaying time
            myTime = date.strftime(date_format)
            date=date.astimezone(timezonte = datetime.now(tz=pytz.utc))

            #Activities is a list--
            #create string for list
            #populate string with variables
            str = f"Earned {goldThisTurn} from this {location} {myTime}"
            #save string to sessions
            activities.append(str)
            request.session['activities'] = activities

    return redirect('/')







# Create your views here.
