from concurrent.futures import ThreadPoolExecutor
import json
import random
import time
import paho.mqtt.client as mqtt
import time


# Define mqtt broker settings
MQTT_BROCKER = "mqtt.eclipseprojects.io"
MQTT_CLIENT = mqtt.Client("car")
MQTT_TOPIC = "car-data"

# connect to MQTT BROCKER
MQTT_CLIENT.connect(MQTT_BROCKER)

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


# Define function to simulate car data
def simulate_car_data(car_id):
    

    # Generate and publish random car data every second
    while True:
        data = generate_car_data(car_id)
        MQTT_CLIENT.publish(MQTT_TOPIC, data)
        print("MQTT: Just published to topic : " +MQTT_TOPIC)
        jdata = json.loads(data)
        string = json.dumps(jdata, indent=4, sort_keys=True)
        print (string)
        time.sleep(1)

# Start threads to simulate car data
with ThreadPoolExecutor(max_workers=NUM_CARS) as executor:
    for i in range(NUM_CARS):
        executor.submit(simulate_car_data, i)
        print("start car ")

