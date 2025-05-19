from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from credenciamento.models import Usuario

def aplicacao_homepage(request):
    return render (request,'aplicacao/homepage.html')

@login_required
def aplicacao_perfil(request):
    # Garante que o usuário do modelo `Usuario` corresponde ao usuário logado
    usuario = Usuario.objects.filter(email=request.user.email).first()

    # Em casos muito raros, pode não encontrar o usuário no modelo customizado
    if not usuario:
        return render(request, 'aplicacao/perfil.html', {'erro': 'Usuário não encontrado.'})

    return render(request, 'aplicacao/perfil.html', {'usuario': usuario})

def aplicacao_excluir(request):
    return render (request,'aplicacao/excluir.html')