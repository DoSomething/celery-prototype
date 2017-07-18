lint:
	pylint blink tests

test:
	pytest

test-with-cov:
	pytest --cov=blink --cov-report html

run-web:
	gunicorn blink.web:app --log-file -

run-celery:
	python run-celery.py worker -n worker1@local --without-mingle --without-heartbeat

watch-celery:
	watchmedo auto-restart --patterns="*.py" --recursive -- make run-celery

watch-web:
	watchmedo auto-restart --patterns="*.py" --recursive -- python run-web.py
