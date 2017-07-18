web: gunicorn blink.web:app --log-file -
worker: python run-celery.py worker -n worker1@heroku --without-mingle --without-heartbeat

