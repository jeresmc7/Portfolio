"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include #Agrego el include para llamar las urls de las apps
# Agregado para las imagenes en media/
from django.conf.urls.static import static
from django.conf import settings

from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Vista inicial de toda la app
    path('blog/', include('blog.urls')), # Incluyo las urls de blog
    #path('portfolio/', include('portfolio.urls')), # Incluyo las urls de blog
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
