from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from credenciamento.models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, logout


def aplicacao_homepage(request):
    return render (request,'aplicacao/homepage.html')

@login_required
def aplicacao_perfil(request):
    # Garante que o usuário do modelo Usuario corresponde ao usuário logado (classe usuario do credenciamento/models)
    usuario = Usuario.objects.filter(email=request.user.email).first()

    # Em casos muito raros, pode não encontrar o usuário no modelo customizado(classe usuario do credenciamento/models)
    if not usuario:
        return render(request, 'aplicacao/perfil.html', {'erro': 'Usuário não encontrado.'})

    return render(request, 'aplicacao/perfil.html', {'usuario': usuario})

def aplicacao_excluir(request):
    return render (request,'aplicacao/excluir.html')




# TENTATIVA DE EXCLUIR CONTA BD
def aplicacao_excluir(request):
    if request.method == 'POST':
        senha = request.POST.get('senha')
        user = request.user
        user_auth = authenticate(username=user.username, password=senha)

        if user_auth:
            try:
                # apaga também o modelo customizado(classe usuario do credenciamento/models)
                Usuario.objects.filter(email=user.email).delete()

                # apaga o usuário do bd
                user.delete()

                logout(request)
                messages.success(request, 'Sua conta foi excluída com sucesso.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Erro ao excluir a conta: {str(e)}')
        else:
            messages.error(request, 'Senha incorreta. Tente novamente.')

    return render(request, 'aplicacao/excluir.html')

# Tentativa de editar o nome da pessoa .
@login_required
def aplicacao_editar(request):
    usuario = Usuario.objects.filter(email=request.user.email).first()

    if not usuario:
        messages.error(request, 'Usuário não encontrado.')
        return redirect('perfil')

    if request.method == 'POST':
        novo_nome = request.POST.get('nome')

        if novo_nome:
            usuario.nome = novo_nome
            usuario.save()
            messages.success(request, 'Nome atualizado com sucesso!')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, insira um nome válido.')

    return render(request, 'aplicacao/editar.html', {'usuario': usuario})
