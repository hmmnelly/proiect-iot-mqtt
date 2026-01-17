# Proiect IoT bazat pe MQTT

Acest proiect implementează un sistem IoT folosind protocolul MQTT pentru
comunicarea între un client embedded și clienți receptori.

## Tehnologii utilizate
- Python (client MQTT)
- Protocol MQTT
- Broker public HiveMQ
- Node-RED
- MQTT Explorer

## Funcționalitate
- Clientul Python se conectează la brokerul MQTT
- Primește mesaje ON / OFF
- Mesajele sunt afișate în Node-RED Dashboard
- Sistemul poate fi monitorizat cu MQTT Explorer

## Structura proiectului
- `mqtt_client.py` – client MQTT în Python
- `node-red-flow.json` – flow Node-RED
- `screenshots/` – capturi ecran

