from django.shortcuts import render
from django.http import HttpResponse

dummyPost = [
    {
        'author': 'Someone',
        'title': 'Blog Post 1',
        'content': 'Something good happen in the end of the tunnel',
        'date_posted': '16 August 2021'
    },
    {
        'author': 'MachineLearning12',
        'title': 'Blog Post 2',
        'content': 'OpenAI will always going to be much better over the time',
        'date_posted': '15 August 2021'
    },
    {
        'author': 'Mohammad Fahmi',
        'title': 'Blog Post 3',
        'content': 'There will always be something good happen',
        'date_posted': '17 August 2021'
    }
]


def home(request) -> HttpResponse:
    return render( request, template_name='main/home.html', context={'posts': dummyPost})


def about(request) -> HttpResponse:
    return render(request, template_name='main/about.html', context={'title': 'About'})
