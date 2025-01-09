
import sqlite3

# Cloudflare D1 SQL Database details
d1_db_path = "a5a53e0b-af35-4f87-89ac-7069f635e54b"

def initialize_influxdb():
    # Connect to Cloudflare D1 (acts as SQLite)
    conn = sqlite3.connect(f"{d1_db_path}.sqlite")
    cursor = conn.cursor()

    # Create a sample table for InfluxDB-style time-series data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS influx_data (
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            metric_name TEXT NOT NULL,
            value REAL NOT NULL
        )
    ''')
    conn.commit()
    print("InfluxDB (via Cloudflare D1) initialized.")

    # Insert sample data
    cursor.execute('''
        INSERT INTO influx_data (metric_name, value) VALUES
        ('temperature', 23.5),
        ('humidity', 55.2)
    ''')
    conn.commit()
    print("Sample data inserted into InfluxDB (D1).")

    # Query and print data
    cursor.execute('SELECT * FROM influx_data')
    for row in cursor.fetchall():
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    initialize_influxdb()
