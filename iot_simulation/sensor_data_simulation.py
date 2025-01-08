
import random
import time
import json

def generate_sensor_data():
    # Simulated sensor data
    sensor_data = {
        'temperature': round(random.uniform(20.0, 35.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'gas_level': round(random.uniform(0.0, 100.0), 2),
        'motion_detected': random.choice([True, False]),
    }
    return sensor_data

if __name__ == '__main__':
    print("Starting IoT sensor data simulation...")
    while True:
        data = generate_sensor_data()
        print(json.dumps(data, indent=4))
        time.sleep(2)  # Simulate a 2-second interval between readings
