#!/usr/bin/python

from flask import *
from flask_sockets import Sockets

app = Flask(__name__,
    static_url_path='',
    static_folder="web")
sockets = Sockets(app)

@sockets.route('/ws')
def websocket(ws):
    while True:
        message = ws.receive()
        ws.send(message)


@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)