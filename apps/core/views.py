from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from apps.job.models import Job

def frontpage(request):
    jobs = Job.objects.all()[0:3]

    return render(request, 'core/frontpage.html', {'jobs': jobs})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})