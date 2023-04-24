from django.contrib import admin
from django.db.models import QuerySet

from .models import Movie, Director


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "year", "budget",]
    list_editable = ["rating", "year", "budget",]
    ordering = ['name']
    search_fields = ('name',)
    list_filter = ('budget', 'rating')
    prepopulated_fields = {
        'slug': ("name",)
    }

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('second_name','first_name','email')
    ordering = ('second_name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
