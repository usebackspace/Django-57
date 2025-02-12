from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1> This is a home page </h1>')

def about(request):
    return HttpResponse('<h1> This is a about page </h1>')

def contact(request):
    return HttpResponse('<h1> This is a contact page </h1>')