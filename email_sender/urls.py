from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('bar/', views.progressBar, name='bar'),
	path('db', views.db_form, name='db_form'),
]