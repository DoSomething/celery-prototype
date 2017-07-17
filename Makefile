lint:
	pylint app tests

test:
	pytest

run-web:
	gunicorn app.web:SERVER --log-file -

run-celery:
	python run-celery.py worker -n worker1@local --without-mingle --without-heartbeat

watch-celery:
	watchmedo auto-restart -- make run-celery

watch-web:
	watchmedo auto-restart -- python run-web.py
