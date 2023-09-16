from flask import Flask
from flask import request as rq
from flask import Response
import json

app = Flask(__name__)

@app.route('/')
def home():
    return json.dumps({'message': 'Hello World'})

@app.route('/day_order', methods=['POST'])
def day_order():
    if 'date' in rq.args:
        date = rq.args.get('date')
        return Response(json.dumps({'recieved': date}), status=200, mimetype='application/json')
    else:
        response = {"status": "error", "msg": "Error in Input Parameters"}
        response = json.dumps(response)
        response = Response(response, status=200, mimetype='application/json')
        return response

if __name__ == '__main__':
    app.run(debug=True)