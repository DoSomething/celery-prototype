web: gunicorn app.web:SERVER --log-file -
worker: celery worker --app=app.workers.CELERY -n worker1@heroku --without-mingle --without-heartbeat

