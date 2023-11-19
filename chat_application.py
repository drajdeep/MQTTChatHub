import paho.mqtt.client as mqtt
import threading

broker_address = "broker.hivemq.com"
broker_port = 1883

# Set your client ID
client_id = "Raj"

# Set your username
username = "Rajdeep Das"

# Change the topic, give an uncommon topic name
topic = "chat"

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.payload.decode())

def publish_message(client):
    while True:
        message = input()
        client.publish(topic, f"{username}: {message}")
        

# Set up the MQTT client
client = mqtt.Client(client_id)
client.username_pw_set(username)
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start the background thread for publishing messages
publish_thread = threading.Thread(target=publish_message, args=(client,))
publish_thread.start()

# Start the MQTT loop to listen for incoming messages
client.loop_forever()