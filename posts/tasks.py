from celery import shared_task
from .models import Upvotes


@shared_task(name="reset_upvotes")
def reset_upvotes(*args, **kwargs):
    Upvotes.objects.all().delete()
