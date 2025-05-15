from django.http import HttpResponse
from django.shortcuts import render


def teste_view(request):
    return HttpResponse("Essa é a rota de teste!")    ;

def home_login(request):
    return render (request,'login.html')

def teste_cadastro(request):
    return render(request,'cadastro.html')

def teste_login(request):
    return render (request,'login.html')