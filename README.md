# MQTT Bioreactor Telemetry System

A demonstration project showcasing MQTT-based telemetry for biomedical reactor monitoring with real-time critical temperature alerts.

## Project Overview

This project simulates an IoT biomedical scenario where a bioreactor device publishes temperature telemetry data via MQTT to a cloud platform. The system monitors temperature readings and automatically flags critical conditions (temperature > 37°C) for alerting.

### Key Components

- **Device Simulator** (`bio_reactor.py`): Simulates a bioreactor device that publishes telemetry data (temperature, status, timestamp) to an MQTT broker
- **Test Automation Framework** (`test_telemetry.py`): Validates message routing, data integrity, and critical condition detection

## Architecture

```
Bioreactor Device (bio_reactor.py)
            ↓
    MQTT Broker (broker.emqx.io)
            ↓
Test Framework / Cloud Platform (test_telemetry.py)
```

**Topic Structure:**
- `miltenyi/lab1/bio_001/telemetry` - Bioreactor telemetry data channel

**Payload Format:**
```json
{
  "device_id": "bio_001",
  "temperature_celsius": 39.5,
  "status": "CRITICAL",
  "timestamp": 1234567890.123
}
```

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone or navigate to the project directory:
```bash
cd path/to/Mqtt_demo_Project
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies

- **paho-mqtt (1.6.1)**: MQTT client library for Python
- **pytest**: Testing framework for automated validation

## Usage

### Running the Device Simulator

Publish simulated bioreactor telemetry data to the MQTT broker:

```bash
python bio_reactor.py
```

**Output:**
```
Publishing data to miltenyi/lab1/bio_001/telemetry...
```

This publishes a single message with:
- Temperature: 39.5°C
- Status: CRITICAL
- Device ID: bio_001

### Running the Test Framework

Validate the telemetry routing and data integrity:

```bash
pytest test_telemetry.py -v
```

**Test Workflow:**
1. Starts a subscriber listening to the telemetry topic
2. Waits 10 seconds for the device to publish data (run `bio_reactor.py` during this window)
3. Verifies:
   - Message successfully received from broker
   - Payload contains required temperature data
   - Temperature reading is accurate (39.5°C)
   - Critical status flag is correctly set

## Quick Start

**Terminal 1** - Start the test listener:
```bash
pytest test_telemetry.py -v
```

**Terminal 2** - Within the 10-second window, publish device data:
```bash
python bio_reactor.py
```

Expected output: `SUCCESS: Message routed correctly and data integrity verified.`

## Key Features

- ✅ Real MQTT Broker Integration (public EMQX broker)
- ✅ JSON-based telemetry payload
- ✅ Automatic critical condition detection
- ✅ Message delivery guarantee (QoS 1)
- ✅ Comprehensive test automation
- ✅ Network latency simulation

## Use Cases

- IoT device telemetry validation
- Medical device monitoring systems
- MQTT protocol demonstration
- Test automation for IoT platforms
- Cloud-to-device communication patterns

## Technical Details

### MQTT Configuration

- **Broker**: broker.emqx.io (public test broker)
- **Port**: 1883 (standard)
- **QoS**: 1 (at least once delivery)
- **Topic**: `miltenyi/lab1/bio_001/telemetry`

### Client IDs

- Device: `Bioreactor_001`
- Test Framework: `Test_Automation_Framework`

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection timeout | Check internet connectivity; verify broker is reachable |
| Test fails - No message received | Run `bio_reactor.py` within the 10-second listening window |
| Message payload errors | Ensure `bio_reactor.py` is publishing valid JSON format |
| Pytest not found | Run `pip install pytest` |

## Future Enhancements

- Add database persistence for telemetry data
- Implement automated alerting system (email/SMS)
- Create real-time dashboard visualization
- Add multiple device support
- Implement local MQTT broker (Mosquitto) option
- Add data aggregation and analytics
- Support for multiple sensor types

## License

This is a demonstration project for educational purposes.

## Notes

- The public MQTT broker (broker.emqx.io) is used for testing only
- Messages are not persisted - they are lost if no subscriber is listening
- For production use, deploy a private MQTT broker
- Consider security implications for real IoT deployments (authentication, encryption)

---


