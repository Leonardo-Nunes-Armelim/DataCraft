"""Gera eventos de caixas e os publica no Kafka.

Instale a dependência antes de executar:
    pip install kafka-python

Configurações opcionais (PowerShell):
    $env:KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
    $env:KAFKA_TOPIC = "robotic-distribution-center-boxes"
    $env:EVENTS_PER_SECOND = "2"
"""

import json
import os
import random
import signal
import sys
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "robotic-distribution-center-boxes")
EVENTS_PER_SECOND = float(os.getenv("EVENTS_PER_SECOND", "2"))

BOX_TYPES = ("A", "B", "C")
COLORS = ("green", "blue", "red", "yellow", "purple", "sky")
running = True


def stop_producer(_signal, _frame):
    """Permite encerrar com Ctrl+C sem perder mensagens pendentes."""
    global running
    running = False


def create_box_event():
    """Cria um evento compatível com robotic_distribution_center_boxes."""
    return {
        "external_box_id": random.randint(1, 1_000_000),
        "box_type": random.choice(BOX_TYPES),
        "color": random.choice(COLORS),
        "position_x": round(random.uniform(5, 1195), 1),
        "position_y": round(random.uniform(5, 695), 1),
    }


def main():
    if EVENTS_PER_SECOND <= 0:
        raise ValueError("EVENTS_PER_SECOND deve ser maior que zero.")

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS.split(","),
        value_serializer=lambda event: json.dumps(event).encode("utf-8"),
        acks="all",
        retries=5,
    )

    print(
        f"Publicando eventos no tópico '{KAFKA_TOPIC}' "
        f"via {KAFKA_BOOTSTRAP_SERVERS} "
        f"(média de {EVENTS_PER_SECOND:g} eventos/s)."
    )

    signal.signal(signal.SIGINT, stop_producer)
    signal.signal(signal.SIGTERM, stop_producer)

    try:
        while running:
            event = create_box_event()
            producer.send(KAFKA_TOPIC, value=event).get(timeout=10)
            print(json.dumps(event, ensure_ascii=False))

            # Distribuição exponencial: intervalo aleatório cuja média é 1 / taxa.
            time.sleep(random.expovariate(EVENTS_PER_SECOND))
    except KafkaError as error:
        print(f"Erro ao publicar no Kafka: {error}", file=sys.stderr)
        sys.exit(1)
    finally:
        producer.flush()
        producer.close()


if __name__ == "__main__":
    main()
