from celery import Celery
import os
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")

app = Celery("proj")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.beat_schedule = {
#     # Scheduler Name
#     "print-message-ten-seconds": {
#         # Task Name (Name Specified in Decorator)
#         "task": "reset_upvotes",
#         # Schedule
#         "schedule": 10.0,
#     }
# }
