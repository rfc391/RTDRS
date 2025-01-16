
import json
import os

# Load Cloudflare Configurations
cloudflare_config_path = "configs/cloudflare_config.json"
with open(cloudflare_config_path, "r") as file:
    cloudflare_config = json.load(file)

CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN", cloudflare_config["CLOUDFLARE_API_TOKEN"])
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID", cloudflare_config["CLOUDFLARE_ACCOUNT_ID"])
CLOUDFLARE_TUNNEL_ID = os.getenv("CLOUDFLARE_TUNNEL_ID", cloudflare_config["CLOUDFLARE_TUNNEL_ID"])

# Load InfluxDB Configurations
influxdb_config_path = "configs/influxdb_config.json"
with open(influxdb_config_path, "r") as file:
    influxdb_config = json.load(file)

INFLUXDB_URL = influxdb_config["INFLUXDB_URL"]
INFLUXDB_TOKEN = influxdb_config["INFLUXDB_TOKEN"]
INFLUXDB_ORG = influxdb_config["INFLUXDB_ORG"]
INFLUXDB_BUCKET = influxdb_config["INFLUXDB_BUCKET"]

# Load immudb Configurations
immudb_config_path = "configs/immudb_config.json"
with open(immudb_config_path, "r") as file:
    immudb_config = json.load(file)

IMMUDB_URL = immudb_config["IMMUDB_URL"]
IMMUDB_USER = immudb_config["IMMUDB_USER"]
IMMUDB_PASSWORD = immudb_config["IMMUDB_PASSWORD"]

# Example usage in a script
def connect_to_influxdb():
    print(f"Connecting to InfluxDB at {INFLUXDB_URL} with bucket {INFLUXDB_BUCKET}")

def connect_to_immudb():
    print(f"Connecting to immudb at {IMMUDB_URL} as user {IMMUDB_USER}")

def setup_cloudflare_tunnel():
    print(f"Using Cloudflare Tunnel ID: {CLOUDFLARE_TUNNEL_ID}")

connect_to_influxdb()
connect_to_immudb()
setup_cloudflare_tunnel()
