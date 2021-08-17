from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request) -> HttpResponse:
    return render(request, template_name='main/home.html', context={'posts': Post.objects.all()})


def about(request) -> HttpResponse:
    return render(request, template_name='main/about.html', context={'title': 'About'})
