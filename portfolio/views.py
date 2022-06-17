from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    # Desde modelos traigo todos los Projects
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects': projects}) # El render ya conoce la carpeta templates
    
