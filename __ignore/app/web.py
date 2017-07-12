from flask import Flask
from app.workers import print_params
from app.workers import gambit_mdata_relay

SERVER = Flask(__name__)


@SERVER.route('/', methods=['GET'])
def get_params():
    print('at=info app=celery request_id=2e3cad7d-b6a3-4f4b-ab66-bae29acafe79 Log stash FTW')
    print_params.apply_async(args=[1])
    return 'Object Created', 201


@SERVER.route('/requests', methods=['GET'])
def get_requests():
    data = {
        'keyword': "BOOKBOT",
        'phone': '13478227222',
        'message_id': '841415468',
        'profile_id': '167181555'
    }
    gambit_mdata_relay.apply_async(args=[data])
    return 'Object Created', 201


if __name__ == ('__main__'):
    SERVER.debug = False
    SERVER.run()