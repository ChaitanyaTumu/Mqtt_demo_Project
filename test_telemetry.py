import paho.mqtt.client as mqtt
import json
import time
import pytest

BROKER = "broker.emqx.io"
TOPIC = "miltenyi/lab1/bio_001/telemetry"

# Global variable to store the message when it arrives
received_message = None

# This function triggers automatically when a message arrives
def on_message(client, userdata, msg):
    global received_message
    received_message = json.loads(msg.payload.decode())

def test_critical_temperature_routing():
    global received_message
    received_message = None # Reset before test

    # 1. Setup the Subscriber (Acting as the Cloud Platform)
    client = mqtt.Client(client_id="Test_Automation_Framework")
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    
    # 2. Subscribe to the exact topic the bioreactor uses
    client.subscribe(TOPIC)
    client.loop_start() # Start listening in the background

    # 3. Wait for the message to arrive (Simulating network latency)
    # Note: In a real test, the device simulator would be triggered here. 
    # For this project, you will run the device script manually.
    print("\nWaiting 10 seconds for the bioreactor to send data...")
    time.sleep(10) 
    
    client.loop_stop()
    client.disconnect()

    # --- VERIFICATION (The most important part) ---
    
    # Requirement 1: Did the message actually arrive?
    assert received_message is not None, "FAILED: No message received from broker!"

    # Requirement 2: Is the data format correct?
    assert "temperature_celsius" in received_message, "FAILED: Payload missing temperature data!"
    
    # Requirement 3: Did the system correctly flag a temp over 37C as CRITICAL?
    assert received_message["temperature_celsius"] == 39.5, "FAILED: Temperature data corrupted!"
    assert received_message["status"] == "CRITICAL", "FAILED: Status not set to CRITICAL!"
    
    print("SUCCESS: Message routed correctly and data integrity verified.")