from flask import Flask, jsonify
import requests
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
    mylist = requests.get('http://list:8080/list').json() 
    
    myfront = '<h1>meme warehouse</h1>'
    for ele in mylist:
        myfront += '''
            <img src={} width=400px>
            <li> {}
            <li> {}
            <br>
            <br>
        '''.format(
                f'http://{os.environ["HOSTIP"]}:8081/{ele}', 
                ele,
                requests.get(f'http://text:8082/{ele}').text
                )
    return myfront

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
