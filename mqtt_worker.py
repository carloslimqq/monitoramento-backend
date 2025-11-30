"""
Worker MQTT simples que se conecta ao broker, escuta o tópico "sensores/#"
e salva mensagens no banco de dados.

Formato esperado do payload: "maquina,parametro,valor"
Exemplo: "laser,temperatura,350.5"
"""
import paho.mqtt.client as mqtt
import os
from database import SessionLocal
from models import Leitura
import time

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_USER = os.getenv("MQTT_USER", None)
MQTT_PASS = os.getenv("MQTT_PASS", None)
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "sensores/#")

def salvar_no_banco(maquina, parametro, valor):
    db = SessionLocal()
    try:
        registro = Telemetria(
            maquina=maquina,
            parametro=parametro,
            valor=float(valor)
        )
        db.add(registro)
        db.commit()
    except Exception as e:
        print("Erro ao salvar no banco:", e)
        db.rollback()
    finally:
        db.close()

def on_connect(client, userdata, flags, rc):
    print("Conectado ao MQTT broker com código:", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8', errors='ignore').strip()
    print(f"Mensagem recebida em {msg.topic}: {payload}")
    try:
        parts = payload.split(",")
        if len(parts) >= 3:
            maquina = parts[0].strip()
            parametro = parts[1].strip()
            valor = parts[2].strip()
            salvar_no_banco(maquina, parametro, valor)
        else:
            print("Payload no formato inválido. Esperado: maquina,parametro,valor")
    except Exception as e:
        print("Erro processando mensagem:", e)

def main():
    client = mqtt.Client()
    if MQTT_USER and MQTT_PASS:
        client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
    print("Worker MQTT rodando... (pressione Ctrl+C para sair)")
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Encerrando worker...")

if __name__ == "__main__":
    main()
