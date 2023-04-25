from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movie/<slug:slug_movie>', views.about_movie, name='about'),
    path('directors/', views.directors, name='directors'),
    path('directors/<int:director_id>',views.about_director,name='about_director'),
]
