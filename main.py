from flask import Flask
from flask import Response
import json
import day_order_dates
from flask_cors import CORS

app = Flask(__name__)
dod = day_order_dates.DayOrderDates()
dataVersion = 2

CORS(app)


@app.route('/')
def home():
    return json.dumps({"message": "Hello World"})

@app.route('/check_version', methods=['GET'])
def day_order():
    return Response(json.dumps({"status": "success", "dataVersion": dataVersion}), status=200, mimetype='application/json')

@app.route('/day_order_dates', methods=['GET'])
def day_order_dates():
    try:
        data = dod.getDayOrderDates()
        response = Response(json.dumps(data), status=200, mimetype='application/json')
        return response
    except:
        data = {"status": "success", "msg": "Error in retriving data"}
        response = Response(json.dumps(data), status=200, mimetype='application/json')
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)