from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('django_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')


"""
app.conf.beat_schdule = {
    'add-two-numbers-after-5-seconds': {
        'task': 'celeryApp.tasks.add',
        'schedule': 5,
        'args': (10,10),
    }
}
"""

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')