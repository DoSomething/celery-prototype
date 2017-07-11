import json

from celery import Celery
import requests

from config.gambit import gambit_config

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
    response = requests.post(
        f'{gambit_config["base_url"]}/chatbot',
        data=json.dumps(data),
        headers=get_gambit_headers()
    )

    if response.status_code == 200:
        print(response.json())
        return True

    print(response)
    print(response.text)

def get_gambit_headers():
    return {
        'x-gambit-api-key': gambit_config['api_key'],
        'Content-type': 'application/json',
    }
