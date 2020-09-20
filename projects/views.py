from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() #This line of code grabs everything from the database and turns them into python objects and then puts them into a list
    return render(request, 'projects/home.html', {'projects':projects})

def about(request):
    return render(request, 'projects/about_me.html')