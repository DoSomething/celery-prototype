from flask import Flask
from workers import print_params

SERVER = Flask(__name__)

@SERVER.route('/', methods=['GET', 'POST'])
def blink():
    print_params.apply_async(args=[1])
    return "Object Created", 201

if __name__ == ("__main__"):
    SERVER.debug = False
    SERVER.run()
