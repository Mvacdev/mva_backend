import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mva_proj.settings")

app = Celery("mva_proj")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

