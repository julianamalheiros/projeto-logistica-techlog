# 🚚 Case TechLog: Otimização Logística com Power BI

## 📌 Sobre o Projeto
Este é um projeto de **Business Intelligence** focado em logística, simulando um cenário real de uma empresa de tecnologia ("TechLog") que enfrenta desafios na entrega de maquininhas de cartão.

O objetivo é transformar dados brutos de entregas em insights acionáveis para reduzir **custos operacionais** e melhorar o **SLA (Service Level Agreement)**.

> **Nota**: Este projeto é educacional. A "TechLog" é uma empresa fictícia e os dados foram gerados sinteticamente para fins de estudo e demonstração de competências em Análise de Dados.

## 💼 O Problema de Negócio
A diretoria da TechLog identificou um aumento expressivo nas reclamações de clientes sobre atrasos e um custo logístico acima do orçado. Os principais sintomas são:

1.  **Ineficiência no Last Mile**: Alto índice de reentregas em certas regiões.
2.  **Custos Variáveis**: Falta de visibilidade sobre quais transportadoras estão performando mal.
3.  **Churn**: Clientes cancelando o serviço antes mesmo de receber a máquina.

## 🎯 Objetivo da Análise
Como Analista de Dados, minha missão foi construir um Dashboard Gerencial para responder:

*   Quais regiões possuem o maior índice de falha na entrega?
*   Qual transportadora tem o melhor custo-benefício?
*   Qual o impacto financeiro das reentregas e devoluções?

## 🛠 Tecnologia Utilizada
*   **Python (Pandas/Numpy)**: Geração e tratamento da massa de dados (ETL).
*   **Power BI**: Modelagem de dados (Star Schema), medidas DAX e visualização.
*   **Excel/CSV**: Fonte de dados.

## 📊 Estrutura dos Dados
O dataset `entregas_techlog.csv` contém 10.000 registros com as seguintes colunas principais:
*   `ID_Pedido`: Identificador único.
*   `Status_Entrega`: Se foi entregue dentro do prazo, atrasado ou devolvido.
*   `Motivo_Falha`: Razão para o insucesso (ex: Cliente Ausente, Endereço Não Localizado).
*   `SLA_Previsto` vs `Dias_Reais`: Comparativo para cálculo de atraso.
*   `Custo_Frete`: Valor pago à transportadora.

## 🗄️ Configuração do Banco de Dados (Opcional - Nível Avançado)
Para um portfólio de alto nível, recomendamos carregar os dados no **MySQL** antes de conectar no Power BI.

1.  Instale o MySQL Workbench.
2.  Abra o arquivo `setup_database.sql` e execute para criar o banco `techlog_db`.
3.  Abra o arquivo `insert_data.sql` e execute para carregar os 10.000 registros.
    *   *Nota: O script de insert pode demorar alguns segundos.*

## 🚀 Como Executar
### Opção A: Via CSV (Simples)
1.  Baixe o arquivo `entregas_techlog.csv`.
2.  Importe no Power BI via "Texto/CSV".

### Opção B: Via MySQL (Recomendado)
1.  Siga os passos de configuração do banco acima.
2.  No Power BI, clique em **Obter Dados** -> **Banco de Dados MySQL**.
3.  Servidor: `localhost`, Banco: `techlog_db`.
4.  Siga as instruções do `GUIA_POWER_BI.md`.
