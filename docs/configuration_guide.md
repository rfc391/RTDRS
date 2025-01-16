
## Configuration Details

### Cloudflare Zero Trust
To set up Cloudflare Zero Trust for secure connections:
1. Log in to your Cloudflare account and create an API token with the required permissions.
2. Retrieve your account ID and tunnel ID from your Cloudflare dashboard.
3. Replace the placeholders in `configs/cloudflare_config.json`:
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID`
   - `CLOUDFLARE_TUNNEL_ID`

### InfluxDB (Cloudflare D1)
1. Create a bucket and API token in InfluxDB (Cloudflare D1).
2. Replace the placeholders in `configs/influxdb_config.json`:
   - `INFLUXDB_URL`
   - `INFLUXDB_TOKEN`
   - `INFLUXDB_ORG`
   - `INFLUXDB_BUCKET`

### immudb (Cloudflare D2)
1. Set up immudb locally or on Cloudflare D2.
2. Replace the placeholders in `configs/immudb_config.json`:
   - `IMMUDB_URL`
   - `IMMUDB_USER`
   - `IMMUDB_PASSWORD`

Ensure all configurations are secure and stored in environment variables or secrets management systems for production deployments.
