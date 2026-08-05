"""Consome eventos Kafka e grava na tabela robotic_distribution_center_boxes.

Dependências:
    pip install kafka-python "psycopg[binary]"

Exemplo de configuração no PowerShell:
    $env:POSTGRES_PASSWORD = "sua_senha"
    $env:POSTGRES_PORT = "5433"
    py cosumer.py
"""

import json
import os
import sys

import psycopg
from kafka import KafkaConsumer
from kafka.errors import KafkaError


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "robotic-distribution-center-boxes")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "datacraft-boxes-postgres-ingestor")

POSTGRES_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB", "datacraft"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST", "127.0.0.1"),
    "port": os.getenv("POSTGRES_PORT", "5433"),
}

INSERT_BOX_SQL = """
    INSERT INTO robotic_distribution_center_boxes
        (external_box_id, box_type, color, position_x, position_y)
    VALUES
        (%(external_box_id)s, %(box_type)s, %(color)s, %(position_x)s, %(position_y)s)
"""

REQUIRED_FIELDS = {
    "external_box_id",
    "box_type",
    "color",
    "position_x",
    "position_y",
}


def validate_event(event):
    missing_fields = REQUIRED_FIELDS - event.keys()
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Evento sem os campos obrigatórios: {missing}")


def main():
    if not POSTGRES_CONFIG["password"]:
        raise ValueError(
            "Defina POSTGRES_PASSWORD antes de iniciar o consumidor. "
            'Exemplo: $env:POSTGRES_PASSWORD = "sua_senha"'
        )

    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS.split(","),
        group_id=KAFKA_GROUP_ID,
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    )

    print(
        f"Consumindo '{KAFKA_TOPIC}' e inserindo em "
        f"{POSTGRES_CONFIG['dbname']}.robotic_distribution_center_boxes."
    )

    try:
        with psycopg.connect(**POSTGRES_CONFIG) as connection:
            for message in consumer:
                event = message.value
                try:
                    validate_event(event)
                    with connection.cursor() as cursor:
                        cursor.execute(INSERT_BOX_SQL, event)
                    connection.commit()

                    # Só confirma o offset após o commit no PostgreSQL.
                    consumer.commit()
                    print(f"Inserido no PostgreSQL: {json.dumps(event)}")
                except (ValueError, psycopg.Error) as error:
                    connection.rollback()
                    print(
                        f"Erro no evento do offset {message.offset}: {error}",
                        file=sys.stderr,
                    )
    except (KafkaError, psycopg.Error) as error:
        print(f"Erro de conexão: {error}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nConsumidor encerrado.")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
