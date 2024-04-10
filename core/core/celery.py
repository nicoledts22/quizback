from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece la configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Crea una instancia de la aplicación Celery
app = Celery('core')

# Carga la configuración de Celery desde la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre y registra automáticamente tareas desde todos los módulos de Django
app.autodiscover_tasks()