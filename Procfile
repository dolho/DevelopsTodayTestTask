web: gunicorn  test_task.wsgi
worker: celery -A test_task worker --beat -l info

