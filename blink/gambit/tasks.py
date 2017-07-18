import json
import requests

from blink.celery import app
from . import config

@app.task(bind=True, default_retry_delay=1)
def print_params(self, param):
    print(param)
    if param > 5:
        self.retry(max_retries=5)
    else:
        return True


@app.task(bind=True)
def gambit_mdata_relay(self, data):
    response = False
    try:
        response = requests.post(
            f'{config["base_url"]}/chatbot',
            data=json.dumps(data),
            headers=get_gambit_headers()
        )
    except Exception as err:
        print("OS error: {0}".format(err))
        self.retry(max_retries=5, countdown=1)
        return False

    if response.status_code == 500:
        self.retry(max_retries=5)
        return False

    if response.status_code != 200:
        print(response)
        print(response.text)
        return False

    print(response.json())
    return True


def get_gambit_headers():
    return {
        'x-gambit-api-key': config['api_key'],
        'Content-type': 'application/json',
    }
