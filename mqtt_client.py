import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "home/light/living/cmd"

def on_connect(client, userdata, flags, rc):
    print("Conectat la broker MQTT, cod:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    mesaj = msg.payload.decode()
    print(f"Mesaj primit: {mesaj}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
print("Aștept mesaje ON / OFF...")
client.loop_forever()
