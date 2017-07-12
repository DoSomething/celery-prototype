from blink.celery import get_app
from config import load_env

if __name__ == '__main__':
    load_env()
    get_app().start()
