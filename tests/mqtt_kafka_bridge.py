import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import time
import json

MQTT_TOPIC = "car-data"

# Define kafka broker settings
KAFKA_BROKER_ADDRESS = "localhost"
KAFKA_BROKER_PORT = 9092
KAFKA_TOPIC = "car-data"

# Define mqtt broker settings
MQTT_BROCKER = "mqtt.eclipseprojects.io"
MQTT_CLIENT = mqtt.Client("BridgeMQTT2Kafka")
MQTT_TOPIC = "car-data"
MQTT_CLIENT.connect(MQTT_BROCKER)

# creating the producer with synchronous message delivery
kafka_producer = KafkaProducer(
     bootstrap_servers=[KAFKA_BROKER_ADDRESS+":"+str(KAFKA_BROKER_PORT)],
     acks='all',
)

def on_message(client, userdata, message):
   
    jdata = json.loads(message.payload)
    string = json.dumps(jdata, indent=4, sort_keys=True)
    print("Received MQTT message: ")
    #kafka_producer.produce(message.payload)
    kafka_producer.send(KAFKA_TOPIC, message.payload)
    print("KAFKA: Just published to topic"+KAFKA_TOPIC)
    print (string)

MQTT_CLIENT.loop_start()
MQTT_CLIENT.subscribe(MQTT_TOPIC)
MQTT_CLIENT.on_message = on_message
time.sleep(300)
MQTT_CLIENT.loop_end()