from email.mime import image
from django.db import models

#from django.forms import CharField, ImageField, URLField
# Con este .forms me tiraba error de argumentos
from django.db.models.fields.files import ImageField
from django.db.models.fields import CharField, URLField

# Project hereda de models.Model

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
