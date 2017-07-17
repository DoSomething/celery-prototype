from flask import Blueprint
from flask import request

from .tasks import gambit_mdata_relay

web = Blueprint('gambit', __name__)

@web.route('/')
def index():
    return 'Gambit'


@web.route('/mdata', methods=('POST',))
def mdata():
    data = request.get_json(force=True)
    gambit_mdata_relay.apply_async(args=(data,))
    return 'Done', 201
