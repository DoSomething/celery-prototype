from flask import Flask
from flask import request
from workers import print_params

web = Flask(__name__)

@web.route('/', methods=['GET', 'POST'])
def blink():
    print_params.apply_async(args=[request.remote_addr])
    return "Object Created", 201

if __name__ == ("__main__"):
    web.debug = False
    web.run()
