from celery import Celery
import os

# from celery.signals import worker_process_init
# from celery.signals import worker_process_shutdown


# import config

# conn = None

app = Celery('workers', broker=os.environ['BROKER_URI'])

@app.task
def print_params(params):
    print(params)
