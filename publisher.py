import paho.mqtt.client as mqtt
import sys

BROKER = "broker.hivemq.com"
TOPIC = "home/light/living/cmd"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

if len(sys.argv) < 2:
    print("Folosire: py publisher.py ON sau OFF")
    sys.exit(1)

mesaj = sys.argv[1]
client.publish(TOPIC, mesaj)
print("Mesaj trimis:", mesaj)

client.disconnect()
