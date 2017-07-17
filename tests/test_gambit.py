from celery.exceptions import Retry
from httmock import all_requests, HTTMock
from pytest import raises
import requests

from blink.gambit.tasks import print_params, gambit_mdata_relay


@all_requests
def response_content(url, request):
    return {'status_code': 200,
            'content': '{"data": "1"}'}


@all_requests
def server_error(url, request):
    return {'status_code': 500}


def get_gambit_payload():
    return {
        'keyword': "BOOKBOT",
        'phone': '13478227222',
        'message_id': '841415468',
        'profile_id': '167181555'
    }


def test_gambit_relay():
    with HTTMock(response_content):
        assert gambit_mdata_relay(get_gambit_payload())


def test_gambit_relay_retry():
    with HTTMock(server_error):
        with raises(Retry):
            gambit_mdata_relay(get_gambit_payload())
