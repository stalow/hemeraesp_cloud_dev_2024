from flask import Flask
import paho.mqtt.client as mqtt


app = Flask(__name__)

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
mqtt_client.connect("mqtt", 1883, 60)
mqtt_client.subscribe("/hem/testhem")

# Démarrage du client MQTT en arrière-plan
mqtt_client.loop_start()


@app.route('/')
def hello_world():
    return 'Hello, Docker Compose with Python and Mosquitto!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)