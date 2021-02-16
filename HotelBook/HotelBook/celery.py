import os

from celery.schedules import crontab
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelBook.settings')
app = Celery('HotelBook')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_new_hotels': {
        'task': 'apps.main.tasks.weekly_updates_emails',
        'schedule': crontab(hour=20, minute=30, day_of_week=6),
    },
}


