from celery import Celery
from celery import states

# from celery.signals import worker_process_init
# from celery.signals import worker_process_shutdown


# import config

# conn = None

app = Celery()
app.config_from_object('celeryconfig')

@app.task(bind=True, default_retry_delay=1)
def print_params(self, params):
    self.retry(max_retries=5)
    # self.update_state(state=states.SUCCESS, meta=params)
    # return True
