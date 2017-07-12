import os

from dotenv import find_dotenv, load_dotenv

from blink.celery import get_app


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    get_app().start()
