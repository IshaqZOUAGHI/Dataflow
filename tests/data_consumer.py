from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'car-data',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
)


for message in consumer:
    print (message.offset)
    print (message.value)
