import os
from celery import Celery
from django.conf import settings

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_processor.settings')
    app = Celery('video_processor')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
except Exception as e:
    print(e, 'error')