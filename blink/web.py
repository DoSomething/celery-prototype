from flask import Flask
from blink.core.web_dispatcher import webhooks

app = Flask(__name__)
# app.register_blueprint(webhooks, url_prefix='/api/v1/webhooks')


@app.route('/api/v1/webhooks/', methods=['GET'])
def index_webhooks():
    return 'List all webhooks'


@app.route('/', methods=['GET'])
def root(): return 'Hello from Blink'
