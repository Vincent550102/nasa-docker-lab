from flask import Flask, send_file, abort
import requests
import json

app = Flask(__name__)

@app.route('/<text>')
def index(text):
    if text in requests.get('http://list:8080/list').json() and text in json.load(open('./text.json')):
        return json.load(open('./text.json'))[text]
    else:
        abort(404)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
