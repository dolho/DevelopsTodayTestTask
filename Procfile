web: gunicorn  test_task.wsgi
worker: celery -A test_task beat -l info
worker2: celery -A test_task worker -l info

