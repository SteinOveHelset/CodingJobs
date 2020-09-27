from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    return render(request, 'core/signup.html')