from flask import Flask
from flask import request as rq
from flask import Response
import json
import day_order_dates

app = Flask(__name__)
dod = day_order_dates.DayOrderDates()

@app.route('/')
def home():
    return json.dumps({"message": "Hello World"})

@app.route('/day_order', methods=['POST'])
def day_order():
    if 'date' in rq.args:
        data = dod.getDayOrder(rq.args.get('date'))
        return Response(json.dumps({"day_order": data}), status=200, mimetype='application/json')
    else:
        data = json.dumps({"status": "error", "msg": "Error in Input Parameters"})
        response = Response(data, status=200, mimetype='application/json')
        return response



if __name__ == '__main__':
    app.run(debug=True)