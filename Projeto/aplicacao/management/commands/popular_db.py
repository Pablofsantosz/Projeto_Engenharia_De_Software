from django.core.management.base import BaseCommand
from aplicacao.models import CID, ReceitaTemplate

class Command(BaseCommand):
    help = 'Popula o banco de dados com CIDs e Modelos de Receita iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando o processo de popular o banco de dados...'))

        # --- 1. Criando os CIDs ---
        # Usamos get_or_create para não duplicar dados se o comando for rodado mais de uma vez.
        cid_gripe, created_gripe = CID.objects.get_or_create(
            codigo='J06.9',
            defaults={'descricao': 'Infecção aguda das vias aéreas superiores (gripe/resfriado)'}
        )
        if created_gripe:
            self.stdout.write(self.style.SUCCESS(f'CID "{cid_gripe.codigo}" criado.'))

        cid_gastro, created_gastro = CID.objects.get_or_create(
            codigo='A09',
            defaults={'descricao': 'Gastroenterite e colite de origem não especificada (virose)'}
        )
        if created_gastro:
            self.stdout.write(self.style.SUCCESS(f'CID "{cid_gastro.codigo}" criado.'))

        # --- 2. Criando os Modelos de Receita ---
        # Modelo para Gripe
        _, created_template_gripe = ReceitaTemplate.objects.get_or_create(
            cid=cid_gripe,
            titulo='Tratamento Padrão para Gripe/Resfriado',
            defaults={
                'medicamentos': '1. Dipirona Gotas - Dar X gotas por via oral a cada 6 horas, se febre ou dor.\n'
                                '2. Lavagem nasal com soro fisiológico 0,9% - Realizar 3 a 4 vezes ao dia.',
                'orientacoes_gerais': '- Manter repouso relativo.\n'
                                      '- Aumentar a ingestão de líquidos (água, sucos, chás).\n'
                                      '- Retornar se apresentar dificuldade para respirar ou febre persistente por mais de 72h.'
            }
        )
        if created_template_gripe:
            self.stdout.write(self.style.SUCCESS('Modelo de receita para Gripe criado.'))

        # Modelo para Gastroenterite (Virose)
        _, created_template_gastro = ReceitaTemplate.objects.get_or_create(
            cid=cid_gastro,
            titulo='Tratamento Padrão para Virose Gástrica',
            defaults={
                'medicamentos': '1. Soro de Reidratação Oral - Oferecer após cada evacuação líquida ou vômito.\n'
                                '2. Vonau Flash (Ondansetrona) 4mg - 1 comprimido via oral até de 8/8h, se vômitos.',
                'orientacoes_gerais': '- Oferecer dieta leve, com alimentos de fácil digestão (arroz, batata, frango desfiado).\n'
                                      '- Evitar alimentos gordurosos, doces e industrializados.\n'
                                      '- Retornar se houver sinais de desidratação (boca seca, pouca urina, prostração).'
            }
        )
        if created_template_gastro:
            self.stdout.write(self.style.SUCCESS('Modelo de receita para Virose Gástrica criado.'))
            
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))