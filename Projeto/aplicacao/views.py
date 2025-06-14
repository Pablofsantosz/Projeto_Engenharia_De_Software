from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from credenciamento.models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from .models import ReceitaTemplate, Consulta,CID
from django.shortcuts import get_object_or_404, redirect
from .models import ReceitaPersonalizada


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
        novo_email = request.POST.get('email')
        nova_senha = request.POST.get('senha')

        # Atualiza dados
        usuario.nome = novo_nome
        usuario.email = novo_email
        usuario.save()

        # Atualiza também o modelo User padrão do Django
        user = request.user
        user.email = novo_email
        user.username = novo_email  # se você estiver usando email como username
        if nova_senha:
            user.set_password(nova_senha)
        user.save()

        messages.success(request, 'Perfil atualizado com sucesso. Faça login novamente se mudou a senha.')
        return redirect('perfil')

    return render(request, 'aplicacao/editar_perfil.html', {'usuario': usuario})





@login_required
def acessar_receitas(request):
    cids_com_templates = CID.objects.prefetch_related('templates').filter(templates__isnull=False).distinct()
    return render(request, 'aplicacao/acessar_receitas.html', {'cids_com_templates': cids_com_templates})

@login_required
def detalhe_receita(request, template_id):
    template = get_object_or_404(ReceitaTemplate, id=template_id)
    if request.method == 'POST':
        template.titulo = request.POST.get('titulo')
        template.medicamentos = request.POST.get('medicamentos')
        template.orientacoes_gerais = request.POST.get('orientacoes_gerais')
        template.save()
        messages.success(request, 'Receituário atualizado com sucesso!')
        return redirect('detalhe_receita', template_id=template.id)
    return render(request, 'aplicacao/detalhe_receita.html', {'template': template})

@login_required
def imprimir_receita(request, template_id):
    template = get_object_or_404(ReceitaTemplate, id=template_id)
    if request.method == 'POST':
        paciente_nome = request.POST.get('paciente_nome')
        paciente_cpf = request.POST.get('paciente_cpf')
        sintomas = request.POST.get('sintomas')

        # === AQUI A MÁGICA ACONTECE ===
        # Cria o registro da consulta no banco de dados, associado ao médico (request.user)
        Consulta.objects.create(
            medico=request.user,
            paciente_nome=paciente_nome,
            paciente_cpf=paciente_cpf,
            sintomas=sintomas,
            cid_aplicado=template.cid
        )
        # ===============================

        medico_profile = get_object_or_404(Usuario, email=request.user.email)
        context = {
            'template': template,
            'paciente_nome': paciente_nome,
            'paciente_cpf': paciente_cpf,
            'medico': medico_profile,
        }
        return render(request, 'aplicacao/receita_final.html', context)
    return render(request, 'aplicacao/form_impressao.html', {'template': template})

@login_required
def historico_atendimento(request):
    # Filtra as consultas para mostrar APENAS as do médico logado (request.user)
    consultas = Consulta.objects.filter(medico=request.user).order_by('-data_consulta')
    context = {
        'consultas': consultas
    }
    return render(request, 'aplicacao/historico_atendimento.html', context)





@login_required
def gerar_receita(request):
    if request.method == 'POST':
        # ... (coleta de dados do formulário continua a mesma) ...
        paciente_nome = request.POST.get('paciente_nome')
        paciente_cpf = request.POST.get('paciente_cpf')
        paciente_idade = request.POST.get('paciente_idade')
        paciente_peso = request.POST.get('paciente_peso')
        sintomas = request.POST.get('sintomas')
        cid_id = request.POST.get('cid_select')
        titulo_usado = request.POST.get('titulo')
        medicamentos_usados = request.POST.get('medicamentos')
        orientacoes_usadas = request.POST.get('orientacoes')

        if not cid_id:
            messages.error(request, 'Erro: Você deve selecionar um CID para a receita.')
            return redirect('gerar_receita')

        # --- LÓGICA ATUALIZADA AQUI ---

        # 1. VERIFICA SE O MÉDICO QUER SALVAR A RECEITA E A CRIA
        receita_salva = None  # Começa como nulo
        salvar_personalizada = request.POST.get('salvar_personalizada')
        if salvar_personalizada:
            # Cria o objeto e o armazena na variável 'receita_salva'
            receita_salva = ReceitaPersonalizada.objects.create(
                medico=request.user,
                cid_id=cid_id,
                titulo_personalizado=titulo_usado,
                medicamentos_personalizados=medicamentos_usados,
                orientacoes_personalizadas=orientacoes_usadas
            )

        # 2. Salva a consulta, passando a receita que acabamos de criar (ou None, se não foi criada)
        Consulta.objects.create(
            medico=request.user,
            paciente_nome=paciente_nome,
            paciente_cpf=paciente_cpf,
            paciente_idade=paciente_idade,
            paciente_peso=paciente_peso,
            sintomas=sintomas,
            cid_aplicado_id=cid_id,
            receita_gerada=receita_salva  # Conecta a consulta com a receita salva
        )

        # --- FIM DA LÓGICA ATUALIZADA ---

        # 3. Preparar dados e renderizar a página final de impressão (continua igual)
        medico_profile = get_object_or_404(Usuario, email=request.user.email)
        context = {
            'medicamentos': medicamentos_usados,
            'orientacoes': orientacoes_usadas,
            'paciente_nome': paciente_nome,
            'paciente_cpf': paciente_cpf,
            'medico': medico_profile,
        }
        return render(request, 'aplicacao/receita_final_ajustada.html', context)
    
    # ... (o bloco GET continua o mesmo) ...
    else:
        templates_gerais = ReceitaTemplate.objects.all().order_by('cid__codigo', 'titulo')
        receitas_medico = ReceitaPersonalizada.objects.filter(medico=request.user).order_by('titulo_personalizado')
        todos_os_cids = CID.objects.all().order_by('codigo')
        
        context = {
            'templates_gerais': templates_gerais,
            'receitas_personalizadas': receitas_medico,
            'todos_os_cids': todos_os_cids,
        }
        return render(request, 'aplicacao/gerar_receita.html', context)
    
    

@login_required
def ver_receita_salva(request, consulta_id):
    """
    Busca uma consulta e a receita personalizada associada a ela para exibição/impressão.
    """
    # Busca a consulta, garantindo que ela pertence ao médico logado (por segurança)
    consulta = get_object_or_404(Consulta, id=consulta_id, medico=request.user)

    # Verifica se existe uma receita personalizada ligada a esta consulta
    if not consulta.receita_gerada:
        messages.error(request, "Esta consulta não possui uma receita personalizada salva.")
        return redirect('historico_atendimento')

    # Busca os dados do perfil do médico para exibir no receituário
    medico_profile = get_object_or_404(Usuario, email=request.user.email)

    # Prepara o contexto com os dados da receita e do paciente para o template
    context = {
        'medicamentos': consulta.receita_gerada.medicamentos_personalizados,
        'orientacoes': consulta.receita_gerada.orientacoes_personalizadas,
        'paciente_nome': consulta.paciente_nome,
        'paciente_cpf': consulta.paciente_cpf,
        'medico': medico_profile,
    }

    # Reutiliza o mesmo template que a função de gerar receita usa para a impressão final
    return render(request, 'aplicacao/receita_final_ajustada.html', context)