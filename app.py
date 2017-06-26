from flask import Flask

web = Flask(__name__)

@web.route('/', methods=['GET', 'POST'])
def blink():
    return "Object Created", 201

if __name__ == ("__main__"):
    web.debug = False
    web.run()
