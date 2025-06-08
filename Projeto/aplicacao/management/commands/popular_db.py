from django.core.management.base import BaseCommand
from aplicacao.models import CID, ReceitaTemplate

class Command(BaseCommand):
    help = 'Popula o banco de dados com uma lista expandida de CIDs e Modelos de Receita'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Limpando dados antigos e populando o banco de dados...'))

        # --- Criando os CIDs ---
        cid_data = {
            'J06.9': 'Infecção aguda das vias aéreas superiores (gripe/resfriado)',
            'A09': 'Gastroenterite e colite de origem não especificada (virose)',
            'H66.9': 'Otite média, não especificada',
            'J03.9': 'Amigdalite aguda, não especificada',
            'J45.9': 'Asma, não especificada',
            'E11': 'Diabetes mellitus tipo 2'
        }

        cids = {}
        for codigo, descricao in cid_data.items():
            cid, created = CID.objects.get_or_create(codigo=codigo, defaults={'descricao': descricao})
            cids[codigo] = cid
            if created:
                self.stdout.write(self.style.SUCCESS(f'CID "{codigo}" criado.'))

        # --- Criando os Modelos de Receita ---
        templates_data = [
            {
                'cid': cids['J06.9'],
                'titulo': 'Tratamento Padrão para Gripe/Resfriado',
                'medicamentos': '1. Dipirona Gotas - Dar X gotas por via oral a cada 6 horas, se febre ou dor.\n'
                                '2. Lavagem nasal com soro fisiológico 0,9% - Realizar 3 a 4 vezes ao dia.',
                'orientacoes_gerais': '- Manter repouso relativo.\n'
                                      '- Aumentar a ingestão de líquidos.\n'
                                      '- Retornar se febre persistir por mais de 72h.'
            },
            {
                'cid': cids['A09'],
                'titulo': 'Tratamento Padrão para Virose Gástrica',
                'medicamentos': '1. Soro de Reidratação Oral - Oferecer após cada evacuação líquida ou vômito.\n'
                                '2. Vonau Flash (Ondansetrona) 4mg - 1 comprimido via oral até de 8/8h, se vômitos.',
                'orientacoes_gerais': '- Oferecer dieta leve e de fácil digestão.\n'
                                      '- Retornar se houver sinais de desidratação.'
            },
            {
                'cid': cids['H66.9'],
                'titulo': 'Tratamento para Otite Média Aguda',
                'medicamentos': '1. Amoxicilina 50mg/mL - Administrar X mL de 8/8 horas por 7 dias.\n'
                                '2. Ibuprofeno Gotas - Dar X gotas por via oral a cada 8 horas, se dor intensa.',
                'orientacoes_gerais': '- Não introduzir objetos ou líquidos no ouvido.\n'
                                      '- Manter o acompanhamento pediátrico.'
            },
            {
                'cid': cids['J03.9'],
                'titulo': 'Tratamento para Amigdalite Aguda',
                'medicamentos': '1. Penicilina Benzatina (Benzetacil) - Dose única intramuscular (conforme peso).\n'
                                'OU\n'
                                '1. Amoxicilina 250mg/5mL - Administrar X mL de 8/8 horas por 10 dias.',
                'orientacoes_gerais': '- Preferir alimentos líquidos e pastosos frios ou gelados.\n'
                                      '- Manter boa hidratação.'
            },
            {
                'cid': cids['J45.9'],
                'titulo': 'Manejo de Crise de Asma',
                'medicamentos': '1. Salbutamol spray 100mcg/jato (Aerolin) - 4 a 6 jatos com espaçador a cada 20 minutos na primeira hora.\n'
                                '2. Prednisolona 20mg - 1 comprimido por via oral por 5 dias.',
                'orientacoes_gerais': '- Procurar atendimento de emergência imediatamente.\n'
                                      '- Manter a calma e o ambiente arejado.'
            },
            {
                'cid': cids['E11'],
                'titulo': 'Controle Inicial de Diabetes Tipo 2',
                'medicamentos': '1. Metformina 500mg - 1 comprimido por via oral após o café da manhã e o jantar.\n'
                                '2. Glicemia capilar - Verificar 2 vezes ao dia (em jejum e 2h após o almoço).',
                'orientacoes_gerais': '- Acompanhamento com endocrinologista e nutricionista.\n'
                                      '- Iniciar atividade física regular (caminhada de 30 minutos, 5x por semana).'
            }
        ]

        for data in templates_data:
            _, created = ReceitaTemplate.objects.get_or_create(
                cid=data['cid'],
                titulo=data['titulo'],
                defaults={
                    'medicamentos': data['medicamentos'],
                    'orientacoes_gerais': data['orientacoes_gerais']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Modelo de receita para "{data["titulo"]}" criado.'))

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com a nova lista de doenças!'))