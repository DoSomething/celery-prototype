lint:
	pylint app tests

test:
	pytest

run-web:
	gunicorn app.web:SERVER --log-file -

run-worker:
	celery worker --app=app.workers.CELERY -n worker1@local --without-mingle --without-heartbeat

watch-worker:
	watchmedo auto-restart -- celery worker --app=app.workers.CELERY -n worker1@local --without-mingle --without-heartbeat

watch-web:
	watchmedo auto-restart -- gunicorn app.web:SERVER --log-file -
