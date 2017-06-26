from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def blink():
    return "Object Created", 201

if __name__ == ("__main__"):
    app.debug = False
    app.run()
