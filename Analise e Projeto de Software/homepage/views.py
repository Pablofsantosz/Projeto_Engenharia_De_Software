from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome_view (request) :
    return HttpResponse('<h1>Essa é nossa homepage!!<h1/>')

def homepage_paginaInicial(request):
    return render(request, 'homepage/paginaInicial.html')