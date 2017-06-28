from pytest import raises

from celery.exceptions import Retry

from unittest.mock import patch

from ..workers import print_params

class test_print_params:

    def test_success(self):
        assert print_params(1) == True


    def test_retry(self):
        with raises(Retry):
            print_params(10)
