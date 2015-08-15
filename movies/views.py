from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Movie, MovieActor, MovieScreenshot, MovieVideo
from actors.models import Actor
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly

#http://www.django-rest-framework.org/api-guide/viewsets/
# http://www.django-rest-framework.org/api-guide/views/
# Serializers define the API representation.

# ViewSets define the view behavior.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
	
    def list(self, request):
		queryset = Movie.objects.all()
		serializer = MovieSerializer(queryset, many=True)
		return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
    	movie = self.createMovie(request)
    	serializer = MovieSerializer(movie)
    	self.createMovieActor(request, movie)
    	self.createMovieScreenshots(request, movie)
    	self.createMovieTrailers(request, movie)
        return Response(serializer.data)


    def createMovie(self, request):
    	# insert movie
    	id 				= request.POST.get('id', None)
    	name 			= request.data['name']
    	description 	= request.data['description']
    	release_date 	= request.data['release_date']
        obj = Movie.objects.get_or_create(id=id, defaults={'name':name, 'description':description,'release_date':release_date})
        movie = obj[0]
        is_new_record = obj[1]
        if is_new_record == False:#update
			movie.name 			= name
			movie.description 	= description
			movie.release_date 	= release_date
			movie.save()
        return movie

    def createMovieActor(self, request, movie_id):
	    #mapped movie actors

	    actors 	= request.POST.getlist("actors")
	    roles 	= request.POST.getlist("roles")

	    for index, actor in enumerate(actors):
	    	actor = Actor.objects.get(pk=actor)
        	obj = MovieActor.objects.get_or_create(movie_id=movie_id, actor_id=actor, role=roles[index], defaults={'movie_id':movie_id, 'actor_id':actor,'role':roles[index],})
            movie_actor = obj[0]
            is_new_record = obj[1]
            if is_new_record == False:#update
               movie_actor.movie_id 		= movie_id
               movie_actor.actor_id 		= actor
               movie_actor.role 			= roles[index]
               movie_actor.save()

	# add screenshot
    def createMovieScreenshots(self, request, movie_id):
	    #mapped movie actors
    	is_cover_photo 	= request.POST.getlist('is_cover_photo')
    	launched_date 	= request.POST.getlist('launched_date')
    	priority 		= request.POST.getlist('priority')

        files = request.FILES.getlist("banners")
     	for index, file in enumerate(files):
     		if is_cover_photo[index]:
	    	    obj = MovieScreenshot.objects.get_or_create(movie_id=movie_id, 
	    	    	defaults={'file':file, 'is_cover_photo':is_cover_photo[index],'launched_date':launched_date[index],'priority':priority[index],})
	    	    movie_screnshot = obj[0]
	    	    is_new_record = obj[1]
	    	    if is_new_record == False:#update
	    	       movie_screnshot.movie_id 		= movie_id
	    	       movie_screnshot.file 			= file
	    	       movie_screnshot.is_cover_photo 	= is_cover_photo[index]
	    	       movie_screnshot.launched_date 	= launched_date[index]
	    	       movie_screnshot.priority 		= priority[index]
	    	       movie_screnshot.save()

	# add trailers
    def createMovieTrailers(self, request, movie_id):
	    #mapped movie actors
	    #import pdb; pdb.set_trace()
    	launched_date 	= request.POST.getlist('trailer_launched_date')

        files = request.FILES.getlist("trailers")
     	for index, file in enumerate(files):
    	    obj = MovieVideo.objects.get_or_create(movie_id=movie_id, 
    	    	defaults={'file':file, 'launched_date':launched_date[index],})
    	    movie_video = obj[0]
    	    is_new_record = obj[1]
    	    if is_new_record == False:#update
    	       movie_video.movie_id 		= movie_id
    	       movie_video.file 			= file
    	       movie_video.launched_date 	= launched_date[index]
    	       movie_video.save()
