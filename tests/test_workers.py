import os
import sys

from celery.exceptions import Retry
from pytest import raises
from unittest.mock import patch

# Local imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.workers import print_params


def test_success():
    assert print_params(1) == True


def test_retry():
    with raises(Retry):
        print_params(10)
