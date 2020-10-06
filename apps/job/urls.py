from django.urls import path, include

from .views import add_job, job_detail

urlpatterns = [
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/', job_detail, name='job_detail'),
]