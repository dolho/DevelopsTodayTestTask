from celery import shared_task
from .models import Upvotes


@shared_task(name="reset_upvotes")
def reset_upvotes(*args, **kwargs):
    Upvotes.objects.all().delete()

@shared_task(name="log_message")
def reset_upvotes(*args, **kwargs):
    print("Message logged")
