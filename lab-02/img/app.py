from flask import Flask, send_file, abort
import requests

app = Flask(__name__)

@app.route('/<img>')
def index(img):
    if img in requests.get('http://list:8080/list').json():
        return send_file(f'./img/{img}.png', mimetype='image/png')
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
