from pytest import raises

from celery.exceptions import Retry

from app.workers import print_params

def test_success():
    assert print_params(1)

def test_retry():
    with raises(Retry):
        print_params(10)
