from kafka import KafkaProducer
import json
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Define kafka broker settings
KAFKA_BROKER_ADDRESS = "localhost"
KAFKA_BROKER_PORT = 9092
KAFKA_TOPIC = "car-data"

# Define number of cars to simulate
NUM_CARS = 100


# Define function to generate random car data
def generate_car_data(car_id):
    # Generate random car data
    location = {
        "latitude": round(random.uniform(-90, 90), 6),
        "longitude": round(random.uniform(-180, 180), 6)
    }
    data = {
        "car_id": car_id,
        "location": location,
        "speed": random.randint(0, 100),
        "fuel_level": round(random.uniform(0, 1), 2),
        "engine_temperature": round(random.uniform(20, 150), 2),
        "timestamp": int(time.time() * 1000)
    }
    return json.dumps(data).encode('utf-8')

# Define function to publish data to kafka topic
def publish_data(producer, data):
    producer.send(KAFKA_TOPIC, data)
    print(data)

# Define function to simulate car data
def simulate_car_data(car_id):
    # connect to Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092']
    )

    # Generate and publish random car data every second
    while True:
        data = generate_car_data(car_id)
        publish_data(producer, data)
        time.sleep(1)

# Start threads to simulate car data
with ThreadPoolExecutor(max_workers=NUM_CARS) as executor:
    for i in range(NUM_CARS):
        executor.submit(simulate_car_data, i)



