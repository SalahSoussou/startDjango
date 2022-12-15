from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello World from views!!! <div> my div don</div> <p>still ok </p>')
