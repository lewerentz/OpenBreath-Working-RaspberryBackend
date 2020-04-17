from flask import Flask, render_template
app = Flask(__name__)



import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def read_config():
    with open('data.json') as json_file:
        return json.load(json_file)

def write_config(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

@app.route('/config', methods=['GET', 'POST'])
def get_config():
    if request.method == 'POST':
        write_config(request.get_json())

        response = jsonify(read_config())

        return response
    else:
        response = jsonify(read_config())

        return response

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def index():
    return render_template('index.html')
