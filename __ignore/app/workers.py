import json

from celery import Celery
import requests

from config.gambit import gambit_config

CELERY = Celery()
CELERY.config_from_object('celeryconfig')

