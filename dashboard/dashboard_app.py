
from flask import Flask, render_template, jsonify, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Flask app setup
app = Flask(__name__)

# InfluxDB configuration
influxdb_url = "http://localhost:8086"
influxdb_token = "your-influxdb-token"  # Replace with your token
org = "your-org"
bucket = "sensor_data"

client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    try:
        data = request.get_json()
        if data:
            point = Point("iot_sensor_data").field("temperature", data["temperature"])                                              .field("humidity", data["humidity"])                                              .field("gas_level", data["gas_level"])                                              .field("motion_detected", int(data["motion_detected"]))
            write_api.write(bucket=bucket, org=org, record=point)
            return "Data received and stored successfully.", 200
        else:
            return "No data received.", 400
    except Exception as e:
        return str(e), 500

@app.route('/sensor-data', methods=['GET'])
def fetch_sensor_data():
    try:
        query = f'from(bucket: "{bucket}") |> range(start: -1h) |> limit(n: 10)'
        tables = client.query_api().query(query, org=org)
        results = []
        for table in tables:
            for record in table.records:
                results.append(record.values)
        return jsonify(results)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
