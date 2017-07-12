from flask import Blueprint

web = Blueprint('gambit', __name__)

@web.route('/')
def index():
    return 'Gambit'
