from flask import Flask
from flask import request as rq
from flask import Response
import json
import day_order_dates

app = Flask(__name__)
dod = day_order_dates.DayOrderDates()
dataVersion = 1

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
    app.run(debug=True, host='192.168.1.40', port=8080)