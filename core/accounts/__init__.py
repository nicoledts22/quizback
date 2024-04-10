from __future__ import absolute_import, unicode_literals

from celery.contrib.pytest import celery_app

# Importa la aplicación Celery
from .celery import app as celery_app

__all__ = ('celery_app',)