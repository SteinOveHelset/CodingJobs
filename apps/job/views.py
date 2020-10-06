from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AddJobForm
from .models import Job

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'job/job_detail.html', {'job': job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'job/add_job.html', {'form': form})