from django.contrib import admin
from .models import Movie, Actor

# Register your models here.


class ActorsInline(admin.TabularInline):
    model = Movie.actors.through
    extra = 1

class ActorsAdmin(admin.ModelAdmin):
    inlines = [
        ActorsInline,
    ]


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('review', {'fields': ['review']}),

    ]
    inlines = [ActorsInline]
    exclude = ('actors', )

#'''

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorsAdmin)