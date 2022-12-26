from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from myapp.forms import Loger


def home(request):
    form = Loger()
    if request.method == 'POST':
        form = Loger(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'home.html', context)


def sau_hello(request):
    return HttpResponse('Hello World t from views!!! ')


def date(request):
    year = datetime.today()
    week = 'test'
    mydate = {'year': year, 'week': week}
    return render(request, 'date.html', mydate)


def menu(request):
    text = """<h1 style="color: #F4CE14;">  My Menu : </h1>"""
    return HttpResponse(text)


#############################################

def cups(request, cup):
    mycups = {
        'tea': 'ment tea no souger',
        'coffe': 'milck coffe',
        'jous': 'orenge jouse',
    }
    my_pik = mycups[cup]
    return HttpResponse(f"<h2>{cup}</h2>" + my_pik)
