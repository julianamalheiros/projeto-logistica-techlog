# 🚚 Case TechLog: Otimização Logística com Power BI

## Sobre o Projeto
Este projeto eu fiz a partir de um case que recebi durante uma entrevista de emprego! Durante a resolução com os colegas, eu percebi que existiam muitas maneiras de se analisar, muitos possíveis gráficos e possíveis insights e me interessei pra me aprofundar um pouquinho mais após o final da reunião. O foco era a metodologia, a questão era “como fazer”, mas já que não tenho limite de tempo, resolvi pedir ajuda a IA para criar um arquivo .csv de dados fictícios, realizei o tratamento dos dados e toda a parte de Business Intelligence focado em logística, simulando um cenário real de uma empresa de tecnologia ("TechLog") que enfrenta desafios na entrega de maquininhas de cartão.

O objetivo é transformar dados brutos de entregas em insights acionáveis para reduzir custos operacionais e melhorar o SLA (Service Level Agreement).

> **Nota**: Este projeto é educacional. A "TechLog" é uma empresa fictícia e os dados foram gerados sinteticamente para fins de estudo e demonstração de competências em Análise de Dados.

## O Problema de Negócio
A diretoria da TechLog identificou um aumento expressivo nas reclamações de clientes sobre atrasos e um custo logístico acima do orçado. Os principais sintomas são:

*   **Ineficiência no Last Mile**: Alto índice de reentregas em certas regiões.
*   **Custos Variáveis**: Falta de visibilidade sobre quais transportadoras estão performando mal.
*   **Churn**: Clientes cancelando o serviço antes mesmo de receber a máquina.

## Objetivo da Análise
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

## Configuração do Banco de Dados (Opcional - Nível Avançado)
Você pode fazer o projeto subindo o arquivo .csv no power BI, mas particularmente eu prefiro conectá-lo diretamente ao workbench.

## 🚀 Como Executar
### Opção A: Via CSV (Simples)
1.  Baixe o arquivo `entregas_techlog.csv`.
2.  Importe no Power BI via "Texto/CSV".

### Opção B: Via MySQL (Recomendado)
1.  Siga os passos de configuração do banco acima.
2.  No Power BI, clique em **Obter Dados** -> **Banco de Dados MySQL**.
3.  Servidor: `localhost`, Banco: `techlog_db`.

---
Nessa fase, como tinha algumas perguntas básicas pra responder mas posso me aventurar e criar outras métricas, vou subir ao github depois um readme exclusivo para o Power BI e também os gráficos que eu fiz, estou ainda na fase de explorar e buscando novos insights!
