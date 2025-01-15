
# Real-Time Threat Detection and Response System (RTDRS)

The RTDRS is a cutting-edge system designed for real-time detection, analysis, and response to potential threats in public spaces, critical infrastructure, and beyond. 
This project leverages AI, blockchain, IoT sensors, and quantum-safe cryptography to provide a robust counter-terrorism solution.

## Features
- **AI Threat Detection**: Real-time object detection and behavioral analysis using OpenCV.
- **Blockchain Framework**: Immutable and secure data logging with smart contracts for inter-agency collaboration.
- **IoT Simulation**: Mock sensor data for testing temperature, gas levels, motion detection, and more.
- **Real-Time Dashboard**: Web-based visualization of sensor data and alerts.
- **Quantum Cryptography Simulation**: Secure communication protocols.

## Project Structure
```
RTDRS/
├── ai/                # AI models and scripts for threat detection
│   └── object_detection.py
├── blockchain/        # Blockchain framework
│   └── blockchain_framework.py
├── dashboard/         # Frontend and backend for real-time dashboard
│   ├── dashboard_app.py
│   └── templates/
│       └── index.html
├── iot_simulation/    # IoT sensor data simulation
│   └── sensor_data_simulation.py
├── docs/              # Documentation
│   └── installation_guide.md
└── README.md          # Overview and setup instructions
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Flask
- OpenCV
- Required Python libraries (install using `requirements.txt`)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/RTDRS.git
    cd RTDRS
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the modules:
    - **AI Threat Detection**:
        ```bash
        python ./ai/object_detection.py
        ```
    - **Blockchain Framework**:
        ```bash
        python ./blockchain/blockchain_framework.py
        ```
    - **IoT Simulation**:
        ```bash
        python ./iot_simulation/sensor_data_simulation.py
        ```
    - **Real-Time Dashboard**:
        ```bash
        python ./dashboard/dashboard_app.py
        ```

4. Access the dashboard at `http://localhost:5001`.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.


## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Docker (for InfluxDB setup, optional)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RTDRS-main
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up InfluxDB (optional):
   - Run InfluxDB in Docker:
     ```bash
     docker run -d -p 8086:8086 --name influxdb influxdb:latest
     ```
   - Create a bucket and generate an API token.

### Running the Project
1. Start the IoT simulation module:
   ```bash
   python iot_simulation/sensor_data_simulation.py
   ```
2. Start the dashboard application:
   ```bash
   python dashboard/dashboard_app.py
   ```
3. Access the dashboard in your browser at `http://localhost:5001`.

## Additional Notes
- Update the InfluxDB token and organization details in `dashboard/dashboard_app.py` before running.
- Replace placeholder files for YOLO with actual weights and configuration files.

## Contributing
- Feel free to contribute by submitting issues or pull requests.

