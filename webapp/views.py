from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def webapp_homepage(request):
    return render (request,'homepage.html')


def webapp_perfil(request):
    return render (request,'perfil.html')

def web_delete(request):
    return render (request,'excluir.html')