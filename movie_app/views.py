from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):
    content = {
        "movies" : Movie.objects.all()
    }
    return render(request,'movie_app/index.html',context=content)