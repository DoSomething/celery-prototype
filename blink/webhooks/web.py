from flask import Blueprint

web = Blueprint('webhooks', __name__)

@web.route('/')
def index():
    return 'Webhooks'
