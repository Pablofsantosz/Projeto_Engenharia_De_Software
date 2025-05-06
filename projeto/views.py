from django.http import HttpResponse
from django.shortcuts import render


def teste_view(request):
    return HttpResponse("Essa é a rota de teste!")    ;

def teste_html(request):
    return render(request,'cadastro.html')