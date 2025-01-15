
import random
import time
import json
import requests

# Configuration for integration
API_ENDPOINT = "http://localhost:5000/sensor-data"  # Replace with actual endpoint if available

def generate_sensor_data():
    # Simulated sensor data
    sensor_data = {
        'temperature': round(random.uniform(20.0, 35.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'gas_level': round(random.uniform(0.0, 100.0), 2),
        'motion_detected': random.choice([True, False]),
    }
    return sensor_data

def send_to_dashboard(data):
    try:
        response = requests.post(API_ENDPOINT, json=data)
        if response.status_code == 200:
            print("Data sent to dashboard successfully.")
        else:
            print(f"Failed to send data: {response.text}")
    except Exception as e:
        print(f"Error sending data to dashboard: {str(e)}")

if __name__ == '__main__':
    print("Starting IoT sensor data simulation...")
    while True:
        data = generate_sensor_data()
        print(json.dumps(data, indent=4))  # Output to console
        send_to_dashboard(data)  # Send data to dashboard
        time.sleep(2)  # Simulate a 2-second interval between readings
