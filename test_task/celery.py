from celery import Celery
import os
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")

app = Celery("proj")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
