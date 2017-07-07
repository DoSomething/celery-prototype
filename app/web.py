from flask import Flask
from app.workers import print_params
from app.workers import gambit_mdata_relay

SERVER = Flask(__name__)


@SERVER.route('/', methods=['GET'])
def get_params():
    print_params.apply_async(args=[1])
    return 'Object Created', 201


@SERVER.route('/requests', methods=['GET'])
def get_requests():
    data = {
        'event_id': '1',
        'event_type': '2'
    }
    gambit_mdata_relay.apply_async(args=[data])
    return 'Object Created', 201


if __name__ == ('__main__'):
    SERVER.debug = False
    SERVER.run()
