from django.shortcuts import render
from django.shortcuts import Http404
from django.http import Http404
from django.views import generic
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Movie, Actor
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'web/index.html'


class MoviesView(generic.ListView):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    template_name = 'web/movies.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'web/detail.html'

    def get_queryset(self):
        return Movie.objects.all()


class ActorView(generic.ListView):
    actor_list = Actor.objects.all()
    context = {'actor_list': actor_list}
    template_name = 'web/actors.html'
    context_object_name = 'actor_list'

    def get_queryset(self):
        return Actor.objects.all()


class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'web/actor_detail.html'

    def get_queryset(self):
        return Actor.objects.all()
