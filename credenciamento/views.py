
from django.shortcuts import render, redirect
from .models import Medico
from django.contrib import messages

# Create your views here.


def credenciamento_cadastro(request):
    return render (request,'cadastro.html')




def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        crm = request.POST['crm']
        email = request.POST['email']
        senha = request.POST['senha']  # Ideal: usar hash, mas ok por enquanto

        # Verifica se o e-mail ou CPF já existem
        if Medico.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return redirect('cadastro')
        
        if Medico.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado.")
            return redirect('cadastro')

        Medico.objects.create(
            nome=nome,
            cpf=cpf,
            crm=crm,
            email=email,
            senha=senha  # Ideal: usar make_password
        )
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('login')  # Ajuste para sua rota

    return render(request, 'cadastro.html')









