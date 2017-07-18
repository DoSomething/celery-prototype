from flask import Blueprint
from blink.celery import app
from .tasks import BlinkWebTask

webhooks = Blueprint('webhook', __name__)
@webhooks.route('/')
def index():
    # blink_task_packages =
    for task_name, task in app.tasks.items():
        if isinstance(task, BlinkWebTask):
            print(task_name)
    return 'List all webhooks'

