from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') # El render ya conoce la carpeta templates
    
