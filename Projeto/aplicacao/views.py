from django.shortcuts import render
from django.http import HttpResponse

def aplicacao_homepage(request):
    return render (request,'aplicacao/homepage.html')

def aplicacao_perfil(request):
    return render (request,'aplicacao/perfil.html')

def aplicacao_excluir(request):
    return render (request,'aplicacao/excluir.html')