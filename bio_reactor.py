import paho.mqtt.client as mqtt
import json
import time

# 1. Define the Broker and the Topic
BROKER = "broker.emqx.io"
TOPIC = "miltenyi/lab1/bio_001/telemetry"

def simulate_critical_temp():
    # 2. Create the MQTT client
    client = mqtt.Client(client_id="Bioreactor_001")
    client.connect(BROKER, 1883, 60)

    # 3. Create the fake medical data (JSON format)
    payload = {
        "device_id": "bio_001",
        "temperature_celsius": 39.5,
        "status": "CRITICAL",
        "timestamp": time.time()
    }

    # 4. Publish the data to the broker
    print(f"Publishing data to {TOPIC}...")
    client.publish(TOPIC, json.dumps(payload), qos=1)
    
    # Wait a moment to ensure the message goes through, then disconnect
    time.sleep(2)
    client.disconnect()

if __name__ == "__main__":
    simulate_critical_temp() # main