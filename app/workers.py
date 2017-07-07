from celery import Celery
import requests

CELERY = Celery()
CELERY.config_from_object('celeryconfig')


@CELERY.task(bind=True, default_retry_delay=1)
def print_params(self, param):
    if param > 5:
        self.retry(max_retries=5)
    else:
        return True


@CELERY.task()
def gambit_mdata_relay(data):
    print(data)
