
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor_data', methods=['GET'])
def sensor_data():
    # Simulated sensor data for the dashboard
    data = {
        'temperature': round(random.uniform(20.0, 35.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'gas_level': round(random.uniform(0.0, 100.0), 2),
        'motion_detected': random.choice([True, False]),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
