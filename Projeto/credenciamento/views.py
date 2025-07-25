from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User  # importa o User

# Create your views here.

def credenciamento_cadastro(request):
    if request.method == 'POST':
        # Obter dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        crm = request.POST.get('crm')
        email = request.POST.get('email')
        senha = request.POST.get('senha')  # Ideal: aplicar hash
        
        # print para debbugar
        print(f'Nome: {nome}, CPF: {cpf}, CRM: {crm}, Email: {email}, Senha: {senha}')

        # Validação de CPF e e-mail já existentes
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return redirect('credenciamento:cadastro')
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return redirect('credenciamento:cadastro')
        
        # Criptografando a senha antes de salvar
        senha_hash = make_password(senha)

        # Criar usuário no banco
        try:
            # Cria o usuário do Django para login
            user = User.objects.create_user(username = email, email = email, password = senha)

            usuario = Usuario.objects.create(
                nome = nome,
                cpf = cpf,
                crm = crm,
                email = email,
                senha = senha_hash
            )
            
            
            # print para debbugar
            print(f'Usuário criado com ID: {usuario.id}')

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao salvar o usuário: {str(e)}')

    return render(request, 'credenciamento/cadastro.html')