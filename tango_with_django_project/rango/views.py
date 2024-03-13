from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage':' like a room without a roof!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial was created by James'}
    return render(request, 'rango/about.html')