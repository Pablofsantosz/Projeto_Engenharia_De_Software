from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def projeto_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username = email, password = senha)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')
