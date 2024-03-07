from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Clap along if you feel like happiness is for you <a href='about'>About</a>")

def about(request):
    return HttpResponse("Clap along if you know that happiness is the truth")