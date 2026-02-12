import pandas as pd
import os

def gerar_sql_inserts():
    # Caminhos
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(diretorio_script, 'entregas_techlog.csv')
    caminho_sql = os.path.join(diretorio_script, 'insert_data.sql')

    print(f"Lendo CSV de: {caminho_csv}")
    
    # Ler CSV (pida para tratar NaN como None/NULL do SQL)
    df = pd.read_csv(caminho_csv)
    df = df.where(pd.notnull(df), None)

    print("Gerando comandos SQL...")
    
    with open(caminho_sql, 'w', encoding='utf-8') as f:
        f.write("USE techlog_db;\n\n")
        f.write("DELETE FROM entregas;\n\n") # Limpa tabela antes de inserir
        
        # Gerar INSERTs em lotes para performance
        f.write("INSERT INTO entregas (ID_Pedido, Data_Pedido, Data_Entrega, Status_Entrega, Motivo_Falha, Transportadora, Cidade, UF, Latitude, Longitude, SLA_Previsto_Dias, Dias_Reais_Entrega, Tentativas_Entrega, Valor_Nota, Custo_Frete, SLA_Cumprido) VALUES\n")
        
        valores = []
        for index, row in df.iterrows():
            # Formatar valores para SQL
            def escape_sql(val):
                if val is None:
                    return "NULL"
                if isinstance(val, str):
                    return f"'{val}'"
                return str(val)

            linha_sql = f"({escape_sql(row['ID_Pedido'])}, {escape_sql(row['Data_Pedido'])}, {escape_sql(row['Data_Entrega'])}, {escape_sql(row['Status_Entrega'])}, {escape_sql(row['Motivo_Falha'])}, {escape_sql(row['Transportadora'])}, {escape_sql(row['Cidade'])}, {escape_sql(row['UF'])}, {row['Latitude']}, {row['Longitude']}, {row['SLA_Previsto_Dias']}, {escape_sql(row['Dias_Reais_Entrega'])}, {row['Tentativas_Entrega']}, {row['Valor_Nota']}, {row['Custo_Frete']}, {escape_sql(row['SLA_Cumprido'])})"
            valores.append(linha_sql)
            
            # A cada 1000 linhas, fecha o INSERT e abre outro (evita erro de query muito grande)
            if (index + 1) % 1000 == 0:
                 f.write(",\n".join(valores) + ";\n\n")
                 if (index + 1) < len(df):
                    f.write("INSERT INTO entregas (ID_Pedido, Data_Pedido, Data_Entrega, Status_Entrega, Motivo_Falha, Transportadora, Cidade, UF, Latitude, Longitude, SLA_Previsto_Dias, Dias_Reais_Entrega, Tentativas_Entrega, Valor_Nota, Custo_Frete, SLA_Cumprido) VALUES\n")
                 valores = []

        # Escrever restantes
        if valores:
            f.write(",\n".join(valores) + ";\n")

    print(f"Arquivo SQL gerado com sucesso: {caminho_sql}")

if __name__ == "__main__":
    gerar_sql_inserts()
