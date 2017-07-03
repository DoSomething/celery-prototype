import os

result_backend = os.getenv('RESULT_BACKEND', None)
broker_url = os.getenv('BROKER_URI', 'memory')
# CELERY_ALWAYS_EAGER for tests?

broker_pool_limit = 1 # Will decrease connection usage
broker_heartbeat = None # We're using TCP keep-alive instead
broker_connection_timeout = 30 # May require a long timeout due to Linux DNS timeouts etc
