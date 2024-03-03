import paho.mqtt.client as mqtt
import time

# Callback appelée lorsqu'un message est reçu depuis le topic
def on_message(client, userdata, msg):
    print(f"Message reçu sur le topic {msg.topic}: {msg.payload.decode()}")



# Configuration du client MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

# Connexion au broker MQTT (Mosquitto) avec informations d'identification
mqtt_client.username_pw_set("HEMERAESP", "8J7Nq4e9Ci8wTe")

# Connexion au broker MQTT (Mosquitto)
mqtt_client.connect("172.232.62.233", 1883, 60)
mqtt_client.subscribe("/hem/testhem")

# Démarrage du client MQTT en arrière-plan
mqtt_client.loop_start()
#mqtt_client.loop_forever()


while True:
    time.sleep(1)

