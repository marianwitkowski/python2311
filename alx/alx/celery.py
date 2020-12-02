import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx.settings")

app = Celery('alx')
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
