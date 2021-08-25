from django.shortcuts import render

from .tasks import email_sender, progress_celery
from django_celery.celery import app
from django_celery_results.models import TaskResult


# Create your views here.
def home(request):

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message_content = request.POST['message']

		print(email)

		email_sender.delay(name,email,subject,message_content)

	context = {}

	return render(request, 'email_sender/home.html', context)


def progressBar(request):

	duration = 1

	if not TaskResult.objects.filter(task_args=f'"({duration},)"', status__in=('PROGRESS','PENDING')).exists():
		print("Revoking task for duration :",duration)

		task_bar = progress_celery.delay(1)
		task_id = task_bar.task_id
	else:
		task_id = None
		print("Task is already in queue :",duration)


	print(task_id)



	context = {
		'task_id': task_id,
	}

	return render(request, 'email_sender/progressCustom.html',context)


def db_form(request):

	context = {

	}
	return render(request, 'email_sender/list_save.html', context)