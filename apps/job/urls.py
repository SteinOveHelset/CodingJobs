from django.urls import path, include

from .api import api_search
from .views import add_job, job_detail, apply_for_job, search, edit_job

urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    path('search/', search, name='search'),
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('<int:job_id>/edit/', edit_job, name='edit_job'),
    path('<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job'),
]