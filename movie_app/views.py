from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Movie, Director


# Create your views here.

def index(request):
    context = {
        "movies": Movie.objects.order_by('name'),
        'movies_in_base': Movie.objects.count()
    }
    return render(request, 'movie_app/index.html', context=context)


def about_movie(request, slug_movie: str):
    context = {
        "movie": get_object_or_404(Movie, slug=slug_movie),
    }
    return render(request, 'movie_app/about_movie.html', context=context)


def directors(request):
    context = {
        'directors': Director.objects.order_by('second_name')
    }
    return render(request, 'movie_app/directors.html', context=context)


def about_director(request, director_id):
    director = get_object_or_404(Director,id=director_id)
    movies = director.movie_set.all()
    # topic = Topic.objects.get(id=topic_id)
    # entries = topic.entry_set.order_by('-date_added')
    context = {
        'director': director,
        'movies' : movies,
    }
    return render(request, 'movie_app/about_director.html', context=context)
