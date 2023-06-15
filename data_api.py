from flask import Blueprint, jsonify, current_app

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/api/bulk-data', methods=['GET'])
def get_bulk_data():
    try:
        influx_client = data_blueprint.influx_client
        # Construct the query
        query = f'from(bucket: "{current_app.config["INFLUXDB_BUCKET"]}") |> range(start: 0)'

        # Execute the query
        tables = influx_client.query_api().query(query, org=influx_client.org)

        # Format the result as JSON
        data = []
        for table in tables:
            for record in table.records:
                data_dict = record.values
                data.append(data_dict)

        res_data = {
            "error": False,
            "message": "Data Fetched Successfully",
            "data": data
        }

        return jsonify(res_data), 200
    except Exception as e:
        print(str(e))
        res_data = {
            "error": True,
            "message": "Something Went Wrong",
            "data": None
        }
        return jsonify(res_data), 403
