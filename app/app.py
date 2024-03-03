import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/hem/testhem")

# Callback appelée lorsqu'un message est reçu depuis le topic
def on_message(client, userdata, msg):
    print(f"Message reçu sur le topic {msg.topic}: {msg.payload.decode()}")

print("MQTT sub")

# Configuration du client MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


# Connexion au broker MQTT (Mosquitto) avec informations d'identification
mqtt_client.username_pw_set("HEMERAESP", "8J7Nq4e9Ci8wTe")

# Connexion au broker MQTT (Mosquitto)
mqtt_client.connect("mqtt", 1883, 60)
mqtt_client.subscribe("/hem/testhem")

# Démarrage du client MQTT en arrière-plan
mqtt_client.loop_start()
#mqtt_client.loop_forever()


while True:
    time.sleep(1)

