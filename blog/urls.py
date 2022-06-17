from unicodedata import name
from django.shortcuts import render
from django.urls import path
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'), #Esto es solo para el blog, no la pagina inicial
    # la pagina inicial de blog seria /blog
    path('<int:post_id>', post_detail, name='post_detail')
]
