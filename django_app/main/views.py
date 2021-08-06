from django.shortcuts import render
from django.http import HttpResponse

def home(request) -> HttpResponse :
    return HttpResponse('<h1>Something Good</h1>')
    
def about(request) :
    return HttpResponse('<h2>Mohammad Fahmi</h2>')