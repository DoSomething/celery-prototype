from flask import Blueprint

from .tasks import gambit_mdata_relay

web = Blueprint('gambit', __name__)

@web.route('/')
def index():
    return 'Gambit'


@web.route('/mdata')
def mdata():
    data = {
        'keyword': "BOOKBOT",
        'phone': '13478227222',
        'message_id': '841415468',
        'profile_id': '167181555'
    }
    gambit_mdata_relay.apply_async(args=(data,))
    return 'Done', 201
