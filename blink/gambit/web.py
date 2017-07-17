from flask import Blueprint
from flask import request
from flask import jsonify

from .tasks import gambit_mdata_relay

web = Blueprint('gambit', __name__)

@web.route('/')
def index():
    return 'Gambit'


@web.route('/mdata', methods=('POST',))
def mdata():
    data = request.get_json(force=True, silent=True)
    if data == None:
        # Not parsed
        return jsonify(jsonrpc=2.0), 422

    task_result = gambit_mdata_relay.apply_async(args=(data,))
    response = jsonify(
        jsonrpc=2.0,
        result='success_message_queued',
        id=task_result.id,
    )
    return response, 201
