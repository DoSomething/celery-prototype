from flask import Flask
from flask import request
from app.workers import print_params

server = Flask(__name__)

@server.route('/', methods=['GET', 'POST'])
def blink():
    print_params.apply_async(args=[request.remote_addr])
    return "Object Created", 201

if __name__ == ("__main__"):
    server.debug = False
    server.run()
