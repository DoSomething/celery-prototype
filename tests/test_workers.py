from celery.exceptions import Retry
from httmock import all_requests, HTTMock
from pytest import raises
import requests

from app.workers import print_params, gambit_mdata_relay


@all_requests
def response_content(url, request):
    print(url)
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


def test_success():
    assert print_params(1)


def test_retry():
    with raises(Retry):
        print_params(10)


def test_gambit_relay():
    with HTTMock(response_content):
        result = gambit_mdata_relay(get_gambit_payload())

    assert result


def test_gambit_relay_retry():
    with HTTMock(server_error):
        with raises(Retry):
            gambit_mdata_relay(get_gambit_payload())

