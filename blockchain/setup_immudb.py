
from immudb.client import ImmudbClient
import requests

# immudb configuration
immudb_host = "localhost"
immudb_port = 3322

# Cloudflare R2 details
r2_url = "https://2bf985f6bc3412ca90de78c00002ecaf.r2.cloudflarestorage.com/immudb"
cloudflare_api_key = "SqnVMNvjSXpDN9YCR_vf-cqlnsKjZAcJ4SrfEi5u"

def initialize_immudb():
    # Connect to immudb
    client = ImmudbClient(host=immudb_host, port=immudb_port)
    client.login("immudb", "immudb")  # Default credentials, change as needed.

    # Write test data and verify
    response = client.set(b"key", b"value")
    print("immudb response:", response)

def store_on_r2(data):
    headers = {"Authorization": f"Bearer {cloudflare_api_key}"}
    response = requests.put(r2_url, data=data, headers=headers)
    if response.status_code == 200:
        print("Data stored in R2 successfully.")
    else:
        print(f"Failed to store in R2: {response.text}")

if __name__ == "__main__":
    initialize_immudb()
    store_on_r2(b"Sample data to test integration.")
