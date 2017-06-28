web: gunicorn app.web:server --log-file -
worker: celery worker --app=app.workers.app -n worker1@heroku --without-mingle --without-heartbeat

