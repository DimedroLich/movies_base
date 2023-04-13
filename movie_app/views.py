from django.shortcuts import render,get_object_or_404
from .models import Movie
# Create your views here.

def index(request):
    content = {
        "movies" : Movie.objects.all().order_by('name')
    }
    return render(request,'movie_app/index.html',context=content)

def about_movie(request, slug_movie:str):
    context = {
       "movie": get_object_or_404(Movie,slug=slug_movie),
    }
    return render(request,'movie_app/about_movie.html',context=context)