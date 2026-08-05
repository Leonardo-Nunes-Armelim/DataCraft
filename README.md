# DataCraft
DataCraft é uma plataforma web de ETL e análise de dados que integra as principais etapas de engenharia de dados em um só lugar.
Com ele, você pode conectar fontes de dados, processar em batch e streaming, organizar em um Data Warehouse estruturado e consultar/monitorar os resultados em uma interface unificada.

## O que o DataCraft oferece
- Conexão com Fontes de Dados: suporte a arquivos CSV, APIs e streams em Kafka.
- Orquestração de Pipelines: criação, agendamento e monitoramento de jobs usando Airflow.
- Processamento de Dados:
    - Batch: integração com Spark.
    - Streaming: Kafka + Spark Streaming em tempo real.
- Modelagem de Dados: geração de tabelas fato/dimensão para análises estruturadas (DW).
- Consultas SQL: execução de queries diretamente nos dados já tratados.
- Monitoramento e Logs: visualização em tempo real do status das execuções e saúde dos pipelines.
- Dashboard Básico: métricas e indicadores para acompanhar o fluxo de dados.

## Problemas que o DataCraft resolve
- Automatizar pipelines de ETL em batch e streaming.
- Organizar dados caóticos em um modelo analítico claro (Data Warehouse).
- Permitir que usuários rodem consultas e visualizem resultados sem depender de ferramentas externas.
- Acompanhar em tempo real a execução e a saúde de pipelines de dados.

## Abas / Módulos principais
- Fontes de Dados – cadastrar APIs, arquivos e streams Kafka.
- Pipelines – criar e monitorar fluxos no Airflow.
- Transformações – configurar regras com Spark.
- Streaming – dados em tempo real via Kafka + Spark Streaming.
- Modelagem – visualizar fatos e dimensões do Data Warehouse.
- Consultas SQL – rodar queries nos dados já tratados.
- Monitoramento – acompanhar logs, alertas e status dos jobs.

## Resumindo
O DataCraft é como um mini-Databricks + Airflow + Metabase, mas desenvolvido do zero para demonstrar habilidade prática em engenharia de dados moderna:
- ETL batch e streaming.
- Orquestração de pipelines.
- Modelagem de dados analítica.
- Consulta SQL e monitoramento em uma interface web.

## Como Começar:
    Clone o repositório
    python -m venv ./venv
    .\venv\Scripts\activate.bat
    python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
    cd datacraft
    py manage.py runserver
    Inicie o servidor e comece a explorar!

## Iniciar Projeto existente:
### Windows

    start_datacraft.bat

### Mac/Linux

    ./start_datacraft.sh

## PostgreSQL e variáveis de ambiente

O DataCraft usa PostgreSQL. As credenciais ficam em `datacraft/.env`, fora do código e fora do Git.

1. Entre na pasta que contém o `manage.py`, copie o modelo e informe a sua senha local:

   ```cmd
   cd datacraft
   copy .env.example .env
   notepad .env
   ```

   Preencha `POSTGRES_PASSWORD`. Os demais valores já apontam para o banco local `DataCraft` na porta `5433`.

2. Crie/atualize as tabelas e inicie o Django:

   ```cmd
   py manage.py migrate
   py manage.py runserver
   ```

O arquivo `.env` é específico da sua máquina e não deve ser enviado ao Git. O `.env.example` é o modelo seguro que deve permanecer no projeto.
