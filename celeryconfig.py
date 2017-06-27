import os

result_backend = os.environ['RESULT_BACKEND']
broker_url = os.environ['BROKER_URI']

broker_pool_limit = 1 # Will decrease connection usage
broker_heartbeat = None # We're using TCP keep-alive instead
broker_connection_timeout = 30 # May require a long timeout due to Linux DNS timeouts etc
event_queue_expires = 60 # Will delete all celeryev. queues without consumers after 1 minute.
