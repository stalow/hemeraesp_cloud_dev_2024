import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/hem/endprocess")

# Callback appelée lorsqu'un message est reçu depuis le topic
def on_message(client, userdata, msg):
    print(f"Message reçu sur le topic {msg.topic}: {msg.payload.decode()}")
    if msg.topic == "/hem/endprocess":
        print(f"Message reçu sur le topic {msg.topic}: {msg.payload.decode()}")

        # Nom du fichier CSV
        csv_filename = "/data/donnees.csv"

        # Extraction des données du message MQTT
        payload = msg.payload.decode()

        # Ouvrir le fichier CSV en mode append (ajout)
        with open(csv_filename, mode='a', newline='') as csv_file:
            csv_file.write(f"{msg.payload.decode()}\n")

    if msg.topic == "/hem/getdata":
        # Nom du fichier CSV pour la publication avec le topic "takedata"
        csv_filename = "/data/donnees.csv"

        # Extraction des données du message MQTT
        #payload = msg.payload.decode()

        # Écrire le message dans le fichier CSV avec le topic "takedata"
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_content = csv_file.read()
        client.publish("/hem/rcvdata", csv_content)

print("MQTT sub")

# Configuration du client MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


# Connexion au broker MQTT (Mosquitto) avec informations d'identification
mqtt_client.username_pw_set("HEMERAESP", "8J7Nq4e9Ci8wTe")

# Connexion au broker MQTT (Mosquitto)
mqtt_client.connect("mqtt", 1883, 60)
mqtt_client.subscribe("/hem/endprocess")

# Démarrage du client MQTT en arrière-plan
mqtt_client.loop_start()
#mqtt_client.loop_forever()


while True:
    time.sleep(1)

