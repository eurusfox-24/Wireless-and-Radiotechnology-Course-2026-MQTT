# IoT Telemetry & Edge Communication Node

This repository contains a Python-based implementation of core Internet of Things (IoT) communication architectures. It provides robust examples of MQTT (Message Queuing Telemetry Transport) and direct Socket Programming, designed for edge computing, sensor telemetry, and distributed network applications.

## 📌 Project Overview

This project simulates a comprehensive IoT network architecture, encompassing automated sensor data generation, edge processing, and reliable client-server/publish-subscribe communication models.

### Key Capabilities:
* **MQTT Protocol Integration:** Implements the publish-subscribe messaging pattern for asynchronous, lightweight, and scalable IoT device communication.
* **Direct Socket Streams:** Provides low-level TCP/IP socket programming for dedicated client-server telemetry transmission.
* **Edge Computing Simulation:** Includes an edge node architecture designed to intercept, process, and route data securely between local sensors and centralized brokers/servers.

## 📁 Repository Structure

* `mqtt_publisher.py`: MQTT client service that formats and broadcasts telemetry data to designated broker topics.
* `mqtt_subscriber.py`: MQTT client service configured to listen, ingest, and process data streams from subscribed topics.
* `socketSensor.py`: A lightweight socket client simulating a hardware sensor, transmitting real-time data payloads directly to a central server.
* `socketServer.py`: A socket server designed to listen for incoming sensor connections and process telemetry data.
* `edge_device.py`: A middleware edge node script for bridging local network sensors with wider cloud or broker infrastructure.
* `*.png`: Execution telemetry and system validation logs (`mqtt_pub_ss.png`, `mqtt_sub_ss.png`, `socketSensor screenshot.png`, `socketServer screenshot.png`).

## 🛠️ System Requirements & Setup

This software requires **Python 3.8+** and standard networking dependencies.

**1. Clone the repository:**
```bash
git clone [https://github.com/eurusfox-24/Wireless-and-Radiotechnology-Course-2026-MQTT.git](https://github.com/eurusfox-24/Wireless-and-Radiotechnology-Course-2026-MQTT.git)
cd Wireless-and-Radiotechnology-Course-2026-MQTT
```

**2. Initialize a Virtual Environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install Dependencies:**
The MQTT implementation requires the Eclipse Paho library.
```bash
pip install paho-mqtt
```

## 🚀 Deployment Instructions

### 1. Direct Socket Communication
Launch the server before initiating sensor data streams. Open two separate terminal instances.

**Terminal 1 (Server Node):**
```bash
python socketServer.py
```

**Terminal 2 (Sensor Node):**
```bash
python socketSensor.py
```

### 2. MQTT Publish/Subscribe Architecture
*(Requirement: Ensure access to a local MQTT broker like Eclipse Mosquitto or configure the scripts to target a secure remote broker.)*

Launch the listener before starting the broadcast. Open two separate terminal instances.

**Terminal 1 (Ingestion/Subscriber):**
```bash
python mqtt_subscriber.py
```

**Terminal 2 (Telemetry/Publisher):**
```bash
python mqtt_publisher.py
```

## 📸 System Validation

Refer to the included screenshot artifacts (`*.png`) in the repository root to verify expected terminal outputs and system behaviors against your local deployment.
