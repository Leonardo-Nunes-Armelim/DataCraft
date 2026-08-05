# Random Box Distribution Robot Center

Simulador de eventos de caixas para o DataCraft. Ele gera posições aleatórias de caixas, envia os eventos ao Kafka e grava-os no PostgreSQL por meio de um consumidor.

> Este módulo não expõe uma API HTTP. Ele é uma fonte de dados de streaming para o DataCraft.

## Fluxo

```text
mock.py → Kafka (robotic-distribution-center-boxes) → consumer.py → PostgreSQL
```

- `mock.py`: gera, em média, 2 eventos aleatórios por segundo.
- `consumer.py`: lê cada evento e faz `INSERT` em `robotic_distribution_center_boxes`.
- Kafka: mantém as mensagens entre produtor e consumidor.
- PostgreSQL: banco `DataCraft`, executando localmente na porta `5433`.

Cada mensagem contém:

```json
{
  "external_box_id": 684765,
  "box_type": "B",
  "color": "red",
  "position_x": 722.9,
  "position_y": 406.4
}
```

## Pré-requisitos

- Docker Desktop em execução.
- PostgreSQL local ativo na porta `5433`.
- A tabela `robotic_distribution_center_boxes` já criada no banco `DataCraft`.

## Uso recomendado: Docker Compose

1. Crie a configuração local e informe a senha real do PostgreSQL:

   ```cmd
   copy .env.example .env
   notepad .env
   ```

   Altere apenas `POSTGRES_PASSWORD`. O arquivo `.env` não é enviado ao Git.

2. Inicie Kafka, produtor e consumidor:

   ```cmd
   docker compose up -d --build
   ```

3. Acompanhe o processamento:

   ```cmd
   docker compose logs -f
   ```

   A execução correta mostra eventos no `mock` e linhas `Inserido no PostgreSQL` no `consumer`.

Comandos úteis:

```cmd
docker compose ps                 :: status dos serviços
docker compose restart consumer   :: reinicia somente a gravação no banco
docker compose down               :: para toda a stack
docker compose up -d --build      :: recria após alterar código ou dependências
```

O Compose usa `kafka:9092` entre containers. Para conectar um cliente executado no Windows ao Kafka, use `localhost:29092`.

## Uso manual (para estudar ou depurar)

Deixe somente o Kafka ativo:

```cmd
docker compose up -d kafka
```

No ambiente virtual da API, instale as dependências:

```cmd
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```

Em um terminal, configure a conexão e inicie o consumidor:

```cmd
set "POSTGRES_PASSWORD=sua_senha"
set "POSTGRES_PORT=5433"
set "KAFKA_BOOTSTRAP_SERVERS=localhost:29092"
py consumer.py
```

Em outro terminal, use o mesmo endereço Kafka e inicie o produtor:

```cmd
set "KAFKA_BOOTSTRAP_SERVERS=localhost:29092"
py mock.py
```

Pare qualquer programa com `Ctrl+C`.

## Conferir dados no pgAdmin

No Query Tool do banco `DataCraft`:

```sql
SELECT external_box_id, box_type, color, position_x, position_y
FROM robotic_distribution_center_boxes
LIMIT 20;
```

## Simulação visual opcional

`Robotic_Distribution_Center.py` abre a simulação gráfica com Pygame. Ela é independente do Kafka e não envia eventos para o banco:

```cmd
pip install pygame
py Robotic_Distribution_Center.py
```

## Problemas frequentes

- **Senha inválida no PostgreSQL:** confira `POSTGRES_PASSWORD` no `.env`; depois execute `docker compose up -d --force-recreate`.
- **Kafka não inicia:** confirme que o Docker Desktop está aberto e consulte `docker compose logs kafka`.
- **Eventos chegam ao Kafka mas não ao banco:** consulte `docker compose logs consumer`; o consumidor só confirma a mensagem Kafka depois do `INSERT` funcionar.
