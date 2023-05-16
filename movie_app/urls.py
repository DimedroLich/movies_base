from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movie/<slug:slug_movie>', views.about_movie, name='about'),
    path('directors/', views.Directors.as_view(), name='directors'),
    path('directors/<int:pk>', views.AboutDirector.as_view(), name='about_director'),
    path('actors/', views.Actors.as_view(), name='actors'),
    path('actors/<int:pk>',views.AboutActor.as_view(),name='about_actor'),
]
