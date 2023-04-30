from django.contrib import admin
from django.db.models import QuerySet
from .models import Movie, Director,Actor,DressingRoom


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ["name",'id', "rating", "year", "director",]
    list_editable = ["rating", "director",]
    ordering = ['id']
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
    list_display = ('second_name', 'id','first_name', 'gender')
    list_editable = ('gender',)
    ordering = ('second_name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(DressingRoom)