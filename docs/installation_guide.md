
# Installation Guide

Follow these steps to install and set up the Real-Time Threat Detection and Response System (RTDRS).

## Prerequisites

Before you begin, ensure you have the following installed:
1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
3. **Git**: [Install Git](https://git-scm.com/)
4. **NVIDIA GPU Drivers (Optional)**: Required for GPU-accelerated AI tasks.

## Step 1: Clone the Repository

```bash
git clone https://github.com/rfc391/RTDRS.git
cd RTDRS
```

## Step 2: Set Up Virtual Environment

It is recommended to use a virtual environment to manage Python dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 3: Install Python Dependencies

Use the `requirements.txt` file to install all necessary Python packages.

```bash
pip install -r requirements.txt
```

## Step 4: Configure Services

Refer to the [Configuration Guide](./configuration_guide.md) for details on setting up the following services:
- **Cloudflare Zero Trust**
- **InfluxDB**
- **RabbitMQ**
- **NVIDIA Triton**
- **Redis**
- **IPFS Cluster**

## Step 5: Run the Application

Once all dependencies and services are configured, start the RTDRS application:

```bash
python main.py
```

## Step 6: Verify Installation

Run the health check script to ensure all components are working as expected:

```bash
python scripts/health_check.py
```

## Optional: Docker Deployment

You can deploy the system using Docker for ease of use and scalability.

1. Build the Docker image:
   ```bash
   docker build -t rtdrs-image .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 rtdrs-image
   ```

For advanced deployment instructions, refer to the [Deployment Guide](./deployment_guide.md).

