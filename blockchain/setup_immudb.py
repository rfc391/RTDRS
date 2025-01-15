
from immudb.client import ImmudbClient
import requests
import json

# Load Cloudflare configuration securely
config_path = '../cloudflare_config.json'  # Adjusted path for consistency
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

immudb_host = "localhost"
immudb_port = 3322
r2_url = config['r2_storage_url']
cloudflare_api_key = config['api_key']

def initialize_immudb():
    try:
        # Connect to immudb
        client = ImmudbClient(host=immudb_host, port=immudb_port)
        client.login("immudb", "immudb")  # Change default credentials in production!

        # Write test data and verify
        response = client.set(b"key", b"value")
        print("Immudb response:", response)
    except Exception as e:
        print("Error initializing Immudb:", str(e))

def store_on_r2(data):
    try:
        headers = {"Authorization": f"Bearer {cloudflare_api_key}"}
        response = requests.put(r2_url, data=data, headers=headers)
        if response.status_code == 200:
            print("Data stored in R2 successfully.")
        else:
            print(f"Failed to store in R2: {response.text}")
    except Exception as e:
        print("Error storing data on R2:", str(e))

if __name__ == "__main__":
    initialize_immudb()
    store_on_r2(b"Sample data to test Cloudflare R2 integration")
