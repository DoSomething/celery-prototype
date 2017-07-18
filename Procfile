web: gunicorn app.web:SERVER --log-file -
worker: run-celery.py worker -n worker1@heroku --without-mingle --without-heartbeat

