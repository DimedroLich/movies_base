from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Movie, Director, Actor


# Create your views here.

def index(request):
    context = {
        "movies": Movie.objects.order_by('name'),
        'movies_in_base': Movie.objects.count()
    }
    return render(request, 'movie_app/index.html', context=context)


def about_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        "movie": movie,
        'actors' : movie.actors.all()
    }
    return render(request, 'movie_app/about_movie.html', context=context)


def directors(request):
    context = {
        'directors': Director.objects.order_by('second_name')
    }
    return render(request, 'movie_app/directors_actors.html', context=context)


def about_director(request, director_id):
    director = get_object_or_404(Director,id=director_id)
    movies = director.movie_set.all()
    context = {
        'director': director,
        'movies' : movies,
    }
    return render(request, 'movie_app/about_director.html', context=context)


def actors(request):
    context = {
        'actors' : Actor.objects.all()
    }
    return render(request,'movie_app/directors_actors.html', context=context)


def about_actor(request,actor_id):
    actor = Actor.objects.get(id=actor_id)
    if actor.gender == 'F':
        gender_visualization = 'Женский'
    else:
        gender_visualization = 'Мужской'
    context = {
        "actor": actor,
        "movies" : actor.movie_set.all(),
        'gender' : gender_visualization,
    }
    return render(request, 'movie_app/about_actor.html', context=context)