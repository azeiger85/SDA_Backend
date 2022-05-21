from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# def hello_view(request, s):
#     return HttpResponse(f"Hello {s} world")


def hello_view(request):
    s = request.GET.get('s', '') #value od s  from url encoding or "" by default
    n = request.GET.get('n', 0) #value of n from url encoding or 0 by default
    adjective = "not cloudy"
    
    return render(
        request,
        "hello.html",
        context={"adjectives":[s, n, adjective]}
    )

def index(request):
    return render(request, template_name="base.html")



def movies(request):
#This is the view for the movies
    return render(
    request, template_name='movies.html',
    context={'movies': Movie.objects.all()}
  )


