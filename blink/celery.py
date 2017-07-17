import os
from celery import Celery

app = Celery('blink')

app.config_from_object({
    'result_backend': os.getenv('RESULT_BACKEND', None),
    'broker_url': os.getenv('BROKER_URI', 'memory'),
    'task_default_queue': 'blink',

    'broker_pool_limit': 1, # Will decrease connection usage
    'broker_heartbeat': None, # We're using TCP keep-alive instead
    'broker_connection_timeout': 30, # May require a long timeout due to Linux DNS timeouts etc

    # 'task_serializer': 'json',
    # 'result_serializer': 'json',
    # 'accept_content': ['json'],
})

app.autodiscover_tasks(force=True, packages=(
    'blink.gambit',
));
