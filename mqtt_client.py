import json
import paho.mqtt.client as mqtt
from database import SessionLocal
from models import Leitura

MQTT_HOST = "mosquitto"
MQTT_TOPIC = "sensores/#"

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        db = SessionLocal()

        # Agora capturamos corretamente o campo 'equipamento'
        leitura = Leitura(
            maquina=payload.get("equipamento"),  # atualizado
            dados=payload                         # salva o JSON inteiro
        )

        db.add(leitura)
        db.commit()
        db.close()

        print("Leitura salva:", payload)

    except Exception as e:
        print("Erro ao processar MQTT:", e)


def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message

    client.connect(MQTT_HOST, 1883, 60)
    client.subscribe(MQTT_TOPIC)

    print("MQTT conectado e ouvindo…")
    client.loop_start()

    return client
