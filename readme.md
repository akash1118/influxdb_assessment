# INFLUXDB-PYTHON TASK

#### SETUP INFLUX-DB on Local Using Docker

```
sudo docker run -p 8086:8086 -v myInfluxVolume:/var/lib/influxdb2 influxdb:latest

```

#### Creating a virtual environment:

```sh

conda create -p venv --y

```

#### Installing Required Dependencies:

```sh

pip3 install -r requirements.txt

```
#### Add the Secrets to the Environment Variables

```sh

export INFLUXDB_URL = < DB URL >
export INFLUXDB_TOKEN = <TOKEN>

```
#### Run the APP:

```sh

python3 app.py

```
#### Upload the attached CSV file **air-sensor-data-annotated.csv** to the bucket 'bulk_data':

#### cURL:
```
curl --location --request GET 'http://127.0.0.1:5000/data/api/bulk-data' \
--header 'Content-Type: application/json'

```

Sample Response:
```

{
    "error": false,
    "message": "Data Fetched Successfully"
    "data": [
        {
            "_field": "co",
            "_measurement": "airSensors",
            "_start": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_stop": "Thu, 15 Jun 2023 06:32:34 GMT",
            "_time": "Thu, 15 Jun 2023 03:34:41 GMT",
            "_value": 0.5121152871474747,
            "result": "_result",
            "sensor_id": "TLM0100",
            "table": 0
        },
        {
            "_field": "co",
            "_measurement": "airSensors",
            "_start": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_stop": "Thu, 15 Jun 2023 06:32:34 GMT",
            "_time": "Thu, 15 Jun 2023 03:34:51 GMT",
            "_value": 0.524751710809402,
            "result": "_result",
            "sensor_id": "TLM0100",
            "table": 0
        },
        {
            "_field": "co",
            "_measurement": "airSensors",
            "_start": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_stop": "Thu, 15 Jun 2023 06:32:34 GMT",
            "_time": "Thu, 15 Jun 2023 03:35:01 GMT",
            "_value": 0.5200883097130582,
            "result": "_result",
            "sensor_id": "TLM0100",
            "table": 0
        }
    ]
}

```