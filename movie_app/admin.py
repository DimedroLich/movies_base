from django.contrib import admin
from django.db.models import QuerySet
from .models import Movie, Director,Actor


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "year", "director",]
    list_editable = ["rating", "director",]
    ordering = ['name']
    search_fields = ('name',)
    list_filter = ('budget', 'rating')
    filter_horizontal = ('actors',)
    prepopulated_fields = {
        'slug': ("name",)
    }

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('second_name','first_name','email')
    ordering = ('second_name',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name', 'gender')
    list_editable = ('gender',)
    ordering = ('second_name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor,ActorAdmin)