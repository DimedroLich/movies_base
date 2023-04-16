from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Movie
# Create your views here.

def index(request):
    context = {
        "movies" : Movie.objects.order_by('name'),
        'movies_in_base': Movie.objects.count()
    }
    return render(request,'movie_app/index.html',context=context)

def about_movie(request, slug_movie:str):
    context = {
       "movie": get_object_or_404(Movie,slug=slug_movie),
    }
    return render(request,'movie_app/about_movie.html',context=context)