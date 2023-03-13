from kafka import KafkaConsumer
import json

# Define kafka broker settings
KAFKA_BROKER_ADDRESS = "localhost"
KAFKA_BROKER_PORT = 9092
KAFKA_TOPIC = "car-data"

#creating the producer
kafka_consumer = KafkaConsumer(
    KAFKA_TOPIC,
     bootstrap_servers=[KAFKA_BROKER_ADDRESS+":"+str(KAFKA_BROKER_PORT)],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
)

for message in kafka_consumer:
    print (message.offset)
    jdata = json.loads(message.value)
    string = json.dumps(jdata, indent=4, sort_keys=True)
    print (string)
    
