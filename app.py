from flask import Flask
import os
from influxdb_client import InfluxDBClient
app = Flask(__name__)

# Set the InfluxDB configuration from environment variables
app.config['INFLUXDB_URL'] = os.environ.get('INFLUXDB_URL')
app.config['INFLUXDB_TOKEN'] = os.environ.get('INFLUXDB_TOKEN')
app.config['INFLUXDB_ORG'] = "TEST"
app.config['INFLUXDB_BUCKET'] = "bulk_data"


# Create the InfluxDB client connection
influx_client = InfluxDBClient(
    url=app.config['INFLUXDB_URL'],
    token=app.config['INFLUXDB_TOKEN'],
    org=app.config['INFLUXDB_ORG']
)

# Import the data blueprint
from data_api import data_blueprint

data_blueprint.influx_client = influx_client

# Register the blueprint
app.register_blueprint(data_blueprint, url_prefix='/data')


if __name__ == '__main__':
    app.run(debug=True)