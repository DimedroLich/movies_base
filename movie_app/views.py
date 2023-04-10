from django.shortcuts import render,get_object_or_404
from .models import Movie
# Create your views here.

def index(request):
    content = {
        "movies" : Movie.objects.all()
    }
    return render(request,'movie_app/index.html',context=content)

def about_movie(request, id_movie:int):
    context = {
       "movie": get_object_or_404(Movie,id=id_movie),
    }
    return render(request,'movie_app/about_movie.html',context=context)