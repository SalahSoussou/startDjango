from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from .forms import DemoForm


def home(request):
    return HttpResponse(' <div> my div don</div> <p>still ok </p>')


def sau_hello(request):
    return HttpResponse('Hello World from views!!! ')


def date(request):
    year = datetime.today()
    return HttpResponse(year)


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
