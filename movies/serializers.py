from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Movie, MovieActor, MovieScreenshot, MovieVideo
from actors.models import Actor

#http://www.django-rest-framework.org/api-guide/viewsets/
# http://www.django-rest-framework.org/api-guide/views/
# Serializers define the API representation.
class ActorSerializer(serializers.ModelSerializer):
    launched_date       = serializers.DateField(format=None, input_formats=None)
    class Meta:
        model = Actor
        fields = ('name', 'description', 'launched_date')


class MovieActorSerializer(serializers.ModelSerializer):
    # actor_object              = ActorSerializer(many=True)
    class Meta:
        model = MovieActor
        fields = ('actor_id', 'role', )

class MovieSerializer(serializers.ModelSerializer):
    release_date        = serializers.DateField(format=None, input_formats=None)
    movie_actors        = MovieActorSerializer(many=True)
    movie_screenshots   = serializers.StringRelatedField(many=True)
    movie_trailers      = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'release_date', 'movie_actors', 'movie_screenshots', 'movie_trailers')


