from django.urls import path
from .views import create_job_view


urlpatterns = [
    path('create/', create_job_view, name='create_job')
]