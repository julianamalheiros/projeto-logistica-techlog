# 📈 Guia de Construção: Dashboard Logístico no Power BI

Siga este passo a passo para recriar a solução do case TechLog.


## 1. Importação e Tratamento (ETL)
### Conectando ao Banco de Dados (MySQL)
1.  Abra o Power BI.
2.  Clique em **Obter Dados** -> **Banco de Dados MySQL**.
3.  Preencha:
    *   **Servidor**: `localhost` (ou `127.0.0.1`)
    *   **Banco de Dados**: `techlog_db`
4.  Se pedir credenciais, vá em "Banco de Dados" e coloque seu usuário (ex: `root`) e senha do MySQL.
5.  Selecione a tabela `entregas` e clique em **Transformar Dados**.

### Tratamento (Power Query)
1.  Verifique se os tipos de dados estão corretos (Datas, Decimais).
2.  Substitua valores `null` na coluna `Motivo_Falha` por "Entrega Realizada" (selecione a coluna -> Transformar -> Substituir Valores).
3.  Clique em **Fechar e Aplicar**.

## 2. Modelagem de Dados
Para este case simples, usaremos uma tabela única ("Flatable"), mas para boas práticas, recomenda-se criar uma **Tabela Calendário**:

1.  Vá em **Modelagem** -> **Nova Tabela**.
2.  Cole a fórmula DAX:
    ```DAX
    dCalendario = CALENDAR(MIN('entregas_techlog'[Data_Pedido]), MAX('entregas_techlog'[Data_Entrega]))
    ```
3.  Relacione `dCalendario[Date]` com `entregas_techlog[Data_Pedido]`.

## 3. Principais Medidas DAX
Crie uma nova tabela chamada `_Medidas` para organizar seu código.

### a) Total de Entregas
```DAX
Total Entregas = COUNTROWS('entregas_techlog')
```

### b) Taxa de Sucesso no SLA (%)
```DAX
% Sucesso SLA = 
VAR EntregasNoPrazo = CALCULATE([Total Entregas], 'entregas_techlog'[SLA_Cumprido] = "Sim")
RETURN
DIVIDE(EntregasNoPrazo, [Total Entregas], 0)
```

### c) Total de Custos de Frete
```DAX
Total Frete = SUM('entregas_techlog'[Custo_Frete])
```

### d) Custo Médio por Entrega
```DAX
Custo Médio = AVERAGE('entregas_techlog'[Custo_Frete])
```

### e) % Devoluções/Falhas
```DAX
% Falhas = 
CALCULATE([Total Entregas], 'entregas_techlog'[Status_Entrega] <> "Entregue") / [Total Entregas]
```

## 4. Visualizações Recomendadas

### 🗺️ Página 1: Visão Geográfica
*   **Mapa**: Use as colunas `Latitude` e `Longitude`. Use a medida `% Falhas` na saturação de cor (Bolinhas vermelhas onde falha mais).
*   **Cartões**: Mostre os KPIs principais no topo: Total Entregas, % Sucesso SLA, Custo Total.

### 🚚 Página 2: Performance de Transportadoras
*   **Gráfico de Barras**: Eixo Y = `Transportadora`, Eixo X = `% Sucesso SLA`. (Descubra qual é a pior!).
*   **Matriz**: Linhas = `Transportadora`, Colunas = `Status_Entrega`, Valores = `Total Entregas`.

### ⚠️ Página 3: Análise de Falhas (Pareto)
*   **Gráfico de Árvore de Decomposição (Decomposition Tree)**:
    *   Analisar: `% Falhas`
    *   Explicar por: `Motivo_Falha`, `Cidade`, `UF`.
    *   Isso permite clicar e entender a causa raiz (ex: "Ah, em Manaus o problema é 'Endereço Não Localizado'").

## 5. Dica de Storytelling
Ao apresentar, comece pelo problema macro ("Estamos gastando muito com devoluções") e faça o *drill-down* até a causa ("O problema está concentrado na transportadora 'LogiFast' na região Nordeste").
