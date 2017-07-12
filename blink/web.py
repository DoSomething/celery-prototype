from flask import Flask
from blink.gambit.web import web as gambit
from blink.webhooks.web import web as webhooks

app = Flask(__name__)
app.register_blueprint(gambit, url_prefix='/gambit')
app.register_blueprint(webhooks, url_prefix='/webhooks')

@app.route('/', methods=['GET'])
def root(): return 'Hello from Blink'
