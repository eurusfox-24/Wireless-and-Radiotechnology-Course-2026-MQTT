import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
topic = "savonia/iot/temperature/TEMPP"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker!")
        client.subscribe(topic)  # Subscribe INSIDE on_connect — safest place
    else:
        print("Connection failed, code:", rc)

def on_message(client, userdata, msg):
    value = msg.payload.decode()
    print("Cloud received:", value)

client = mqtt.Client()

client.on_connect = on_connect  # Assign callbacks BEFORE connecting
client.on_message = on_message  # Assign callbacks BEFORE connecting

client.connect(broker, 1883)

client.loop_forever()
