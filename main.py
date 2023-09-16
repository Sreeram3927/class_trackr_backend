from flask import Flask
from flask import request
from flask import Response
import json

app = Flask(__name__)

@app.route('/')
def home():
    return json.dumps({'message': 'Hello World'})

if __name__ == '__main__':
    app.run(debug=True)