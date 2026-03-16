import paho.mqtt.client as mqtt
import random
import time

broker = "broker.emqx.io"
topic = "savonia/iot/temperature/TEMPP"

# Add CallbackAPIVersion to fix the warning
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client.connect(broker, 1883)

while True:
    temperature = round(random.uniform(20, 35), 2)
    client.publish(topic, temperature)
    print("Published to MQTT:", temperature)
    time.sleep(5)
