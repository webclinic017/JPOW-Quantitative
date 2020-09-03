import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JPOW_Quantitative.settings')

app = Celery('JPOW_Quantitative', include = ['jpow_app.updateRetailSentiment', 'jpow_app.updateSPY',])
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'updateRetailSentiment': {
        'task': 'jpow_app.updateRetailSentiment.update',
        'schedule': crontab(hour = '6', day_of_week = 'mon,tue,wed,thu,fri'),
    },
    'updateSPY': {
        'task': 'jpow_app.updateSPY.update',
        'schedule': crontab(hour = '18', day_of_week = 'mon,tue,wed,thu,fri'),
    },
}

app.conf.timezone = 'US/Eastern'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
