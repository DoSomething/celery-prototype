from celery import Celery

# from celery.signals import worker_process_init
# from celery.signals import worker_process_shutdown


# import config

# conn = None

app = Celery('workers')

@app.task
def print_params(params):
    print(params)
