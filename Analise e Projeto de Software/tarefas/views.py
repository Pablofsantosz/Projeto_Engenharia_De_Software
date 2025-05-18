from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.hashers import make_password

# Create your views here.
def tarefas_home(request):
    contexto = {
        'nome': 'Nunno'
    }
    return render(request, 'tarefas/home.html', contexto) # Renderiza a página home.html dentro do template tarefas

''' def tarefas_adicionar(request): 
    return render(request, 'tarefas/adicionar.html') '''

def tarefas_adicionar(request):
    if request.method == 'POST':
        # Obter dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        crm = request.POST.get('crm')
        email = request.POST.get('email')
        senha = request.POST.get('senha')  # Ideal: aplicar hash
        print(f'Nome: {nome}, CPF: {cpf}, CRM: {crm}, Email: {email}, Senha: {senha}')

        # Validação de CPF e e-mail já existentes
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return redirect('tarefas:adicionar')
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return redirect('tarefas:adicionar')
        
        # Criptografando a senha antes de salvar
        senha_hash = make_password(senha)

        # Criar usuário no banco
        try:
            usuario = Usuario.objects.create(
                nome=nome,
                cpf=cpf,
                crm=crm,
                email=email,
                senha=senha_hash
            )
            # Verificando se o usuário foi criado com sucesso
            print(f'Usuário criado com ID: {usuario.id}')

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('tarefas:home')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao salvar o usuário: {str(e)}')

    return render(request, 'tarefas/adicionar.html')