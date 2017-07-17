from blink.utils.config import load_env
load_env()

from blink.celery import app

if __name__ == '__main__':
    app.start()
