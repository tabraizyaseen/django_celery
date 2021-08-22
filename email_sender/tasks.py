from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail

from celery_progress.backend import ProgressRecorder

from time import sleep

@shared_task
def email_sender(name, email, subject, message):
	send_mail(
		subject, 
		f"{message}<br><br><hr />{name}",
		"shahanileader@gmail.com",
		[email],
		fail_silently=False
		)

	return None


@shared_task(bind=True)
def progress_celery(self, duration):
	progress_recorder = ProgressRecorder(self)
	for i in range(30):
		sleep(duration)
		progress_recorder.set_progress(i+1, 30, f'Loop Counter : {i}')
	return 'Done'