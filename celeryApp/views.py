from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	print("print for gunicorn")
	return HttpResponse("<h1>Working Fine</h1>")