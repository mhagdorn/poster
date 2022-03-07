__all__ = ['Config']

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'poster-app-is-not-secret'
    ADMIN = os.environ.get('POSTER_ADMIN') or 'poster@poster.org'

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") or \
        'amqp://guest@localhost//'
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") or \
        'amqp://guest@localhost//'
