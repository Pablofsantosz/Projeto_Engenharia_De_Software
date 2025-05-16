from django.http import HttpResponse
from django.shortcuts import render



def login(request):
    return render (request,'login.html')


# def teste_cadastro(request):
#     return render(request,'cadastro.html')

# def teste_login(request):
#     return render (request,'login.html')

# def teste(request):
#     return render (request,'pagina_principal.html')






