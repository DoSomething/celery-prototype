from flask import Flask
from blink.gambit.web import web as gambit_app

app = Flask(__name__)
app.register_blueprint(gambit_app, url_prefix='/api/v1/gambit')

@app.route('/', methods=['GET'])
def root(): return 'Hello from Blink'
