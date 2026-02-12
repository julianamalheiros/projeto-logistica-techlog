-- Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS techlog_db;
USE techlog_db;

-- Criação da Tabela de Entregas
CREATE TABLE IF NOT EXISTS entregas (
    ID_Pedido VARCHAR(20) PRIMARY KEY,
    Data_Pedido DATE,
    Data_Entrega DATE,
    Status_Entrega VARCHAR(50),
    Motivo_Falha VARCHAR(100),
    Transportadora VARCHAR(50),
    Cidade VARCHAR(100),
    UF CHAR(2),
    Latitude DECIMAL(10, 6),
    Longitude DECIMAL(10, 6),
    SLA_Previsto_Dias INT,
    Dias_Reais_Entrega INT,
    Tentativas_Entrega INT,
    Valor_Nota DECIMAL(10, 2),
    Custo_Frete DECIMAL(10, 2),
    SLA_Cumprido VARCHAR(3)
);
