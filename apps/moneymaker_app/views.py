from django.shortcuts import render, redirect, HttpResponse
from  django.contrib import messages
import random 

def index(request):
    if 'gold_amt' not in request.session:
        request.session['gold_amt'] = 0
        request.session['activities'] = []
    
    return render(request, 'moneymaker_app/index.html')


# Method to add gold 
def process_money(request):
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            request.session['labored'] = 'Farm'
            purse = random.choice(range(10,21))
            request.session['gold_amt'] += purse
            request.session['change'] = purse
        
        elif request.POST['building'] == 'cave':
            request.session['labored'] = 'Cave'
            purse = random.choice(range(5,11))
            request.session['gold_amt'] += purse
            request.session['change'] = purse

        elif request.POST['building'] == 'house':
            request.session['labored'] = 'House'
            purse = random.choice(range(2,6))
            request.session['gold_amt'] += purse
            request.session['change'] = purse

        elif request.POST['building'] == 'casino':
            request.session['labored'] = 'Casino'
            if request.session['gold_amt'] > 50:
                purse = random.choice(range(-50,51))
                request.session['gold_amt'] += purse
                request.session['change'] = purse
            else:
                messages.add_message(request, messages.INFO, 'You must have more than 50 Gold to go to the casino.')
                request.session['change'] = ''
                
                return redirect('/')
                    
    request.session['activities'].append({'gold': request.session['change'], 'building': request.session['labored']})
    
    return redirect('/')