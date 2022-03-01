from flask import Flask, jsonify

import json
app = Flask(__name__)

@app.route('/list')
def index():
    return jsonify(json.load(open("./list.json"))) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
