import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configurações
NUM_REGISTROS = 10000
DATA_INICIO = datetime(2023, 1, 1)
DATA_FIM = datetime(2023, 12, 31)

# Dados Geográficos (Amostra de Cidades Brasileiras e suas Lat/Long aproximadas)
CIDADES = [
    {'Cidade': 'São Paulo', 'UF': 'SP', 'Lat': -23.5505, 'Long': -46.6333, 'Risco': 'Médio'},
    {'Cidade': 'Rio de Janeiro', 'UF': 'RJ', 'Lat': -22.9068, 'Long': -43.1729, 'Risco': 'Alto'},
    {'Cidade': 'Belo Horizonte', 'UF': 'MG', 'Lat': -19.9167, 'Long': -43.9345, 'Risco': 'Baixo'},
    {'Cidade': 'Curitiba', 'UF': 'PR', 'Lat': -25.4284, 'Long': -49.2733, 'Risco': 'Baixo'},
    {'Cidade': 'Porto Alegre', 'UF': 'RS', 'Lat': -30.0346, 'Long': -51.2177, 'Risco': 'Médio'},
    {'Cidade': 'Salvador', 'UF': 'BA', 'Lat': -12.9777, 'Long': -38.5016, 'Risco': 'Alto'},
    {'Cidade': 'Recife', 'UF': 'PE', 'Lat': -8.0476, 'Long': -34.8770, 'Risco': 'Alto'},
    {'Cidade': 'Fortaleza', 'UF': 'CE', 'Lat': -3.7172, 'Long': -38.5434, 'Risco': 'Médio'},
    {'Cidade': 'Brasília', 'UF': 'DF', 'Lat': -15.7975, 'Long': -47.8919, 'Risco': 'Baixo'},
    {'Cidade': 'Manaus', 'UF': 'AM', 'Lat': -3.1190, 'Long': -60.0217, 'Risco': 'Alto'} # Logística complexa
]

TRANSPORTADORAS = ['LogiFast', 'TransRoute', 'EntregaJá', 'FlashLog']
MOTIVOS_FALHA = ['Endereço Não Localizado', 'Cliente Ausente', 'Avaria no Produto', 'Roubo de Carga', 'Veículo Quebrado', 'Área de Risco - Não Atendido']
STATUS_POSSIVEIS = ['Entregue', 'Falha', 'Devolvido']

dados = []

print("Gerando dados...")

for i in range(NUM_REGISTROS):
    # Pedido e Cliente
    id_pedido = f"PED-{100000+i}"
    cidade_info = random.choice(CIDADES)
    
    # Datas
    dias_desde_inicio = (DATA_FIM - DATA_INICIO).days
    data_pedido = DATA_INICIO + timedelta(days=random.randint(0, dias_desde_inicio))
    
    # Transportadora
    transportadora = random.choice(TRANSPORTADORAS)
    
    # Lógica de SLA e Entrega
    sla_previsto = random.randint(2, 10) # Dias úteis prometidos
    
    # Fator de "Problema" baseado na cidade e transportadora
    probabilidade_problema = 0.1 # Base 10%
    if cidade_info['Risco'] == 'Alto':
        probabilidade_problema += 0.15 # +15% de chance de problema
    if transportadora == 'EntregaJá': # Vamos simular que essa é piorzinha
        probabilidade_problema += 0.10

    if random.random() < probabilidade_problema:
        status = random.choice(['Falha', 'Devolvido'])
        motivo_falha = random.choice(MOTIVOS_FALHA)
        dias_reais = sla_previsto + random.randint(5, 15) # Atraso grande
        tentativas = random.randint(2, 5)
    else:
        status = 'Entregue'
        motivo_falha = None
        # Maioria entrega no prazo ou levemente atrasado
        atraso = random.choice([0, 0, 0, 1, -1, -2]) 
        dias_reais = max(1, sla_previsto + atraso)
        tentativas = 1

    data_entrega = data_pedido + timedelta(days=dias_reais) if status == 'Entregue' else None
    
    # Custos
    valor_nota = round(random.uniform(500.0, 5000.0), 2)
    custo_frete = round(valor_nota * random.uniform(0.05, 0.15), 2)
    if status != 'Entregue' or tentativas > 1:
        custo_frete += round(random.uniform(20.0, 50.0) * tentativas, 2) # Custo extra por reentrega


    dados.append({
        'ID_Pedido': id_pedido,
        'Data_Pedido': data_pedido.strftime('%Y-%m-%d'),
        'Data_Entrega': data_entrega.strftime('%Y-%m-%d') if data_entrega else None,
        'Status_Entrega': status,
        'Motivo_Falha': motivo_falha,
        'Transportadora': transportadora,
        'Cidade': cidade_info['Cidade'],
        'UF': cidade_info['UF'],
        'Latitude': cidade_info['Lat'],
        'Longitude': cidade_info['Long'],
        'SLA_Previsto_Dias': sla_previsto,
        'Dias_Reais_Entrega': dias_reais if status == 'Entregue' else None,
        'Tentativas_Entrega': tentativas,
        'Valor_Nota': valor_nota,
        'Custo_Frete': custo_frete,
        'SLA_Cumprido': 'Sim' if (status == 'Entregue' and dias_reais <= sla_previsto) else 'Não'
    })

df = pd.DataFrame(dados)

import os

# Salvar
# O script agora roda dentro da pasta do projeto, então salva no mesmo local
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_script, 'entregas_techlog.csv')

df.to_csv(caminho_arquivo, index=False, encoding='utf-8')

print(f"Arquivo gerado com sucesso: {caminho_arquivo}")
print(df.head())
print(df['Status_Entrega'].value_counts())
