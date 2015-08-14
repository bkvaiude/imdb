from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Movie, MovieActor, MovieScreenshot, MovieVideo

#http://www.django-rest-framework.org/api-guide/viewsets/
# http://www.django-rest-framework.org/api-guide/views/
# Serializers define the API representation.
class MovieListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class MovieListViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Movie.objects.all()
        serializer = MovieListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
    	movie_id = self.createMovie(request)
    	createMovieActor(request, movie_id)

    def createMovie(self, request):
    	# insert movie
	    obj = Movie.objects.get_or_create(id=1, defaults={'name':name, 'description':description,'release_date':release_date})
	    movie = obj[0]
	    is_new_record = obj[1]
	    if is_new_record == False:#update
	       movie.name 			= name
	       movie.description 	= description
	       movie.release_date 	= release_date
	       movie.save()
	    return movie.id

    def createMovieActor(self, request, movie_id):
	    #mapped movie actors
	    actors = request.POST.get("actors",None)
	    roles = request.POST.get("roles",None)
	    for index, actor in actors:
		    obj = MovieActor.objects.get_or_create(movie_id=movie_id, actor_id=actor_id, role=role, defaults={'movie_id':movie_id, 'actor_id':actor_id,'role':role,})
		    movie_actor = obj[0]
		    is_new_record = obj[1]
		    if is_new_record == False:#update
		       movie_actor.movie_id 		= movie_id
		       movie_actor.actor_id 		= actor_id
		       movie_actor.role 			= role
		       movie_actor.save()

	# add screenshot
    def createMovieScreenshots(self, request, movie_id):
	    #mapped movie actors
	    files = request.FILES.get("file[]",None)
	    for file in files:
		    obj = MovieActor.objects.get_or_create(movie_id=movie_id, actor_id=actor_id, role=role, defaults={'movie_id':movie_id, 'actor_id':actor_id,'role':role,})
		    movie_actor = obj[0]
		    is_new_record = obj[1]
		    if is_new_record == False:#update
		       movie_actor.movie_id 		= movie_id
		       movie_actor.file 			= file
		       movie_actor.is_cover_photo 	= role
		       movie_actor.launched_date 	= role
		       movie_actor.priority 		= role
		       movie_actor.save()

	# add trailers
    def createMovieTrailers(self, request, movie_id):
	    #mapped movie actors
	    files = request.POST.get("file[]",None)
	    for index, actor in actors:
		    obj = MovieActor.objects.get_or_create(movie_id=movie_id, actor_id=actor_id, role=role, defaults={'movie_id':movie_id, 'actor_id':actor_id,'role':role,})
		    movie_actor = obj[0]
		    is_new_record = obj[1]
		    if is_new_record == False:#update
		       movie_actor.movie_id 		= movie_id
		       movie_actor.actor_id 		= actor_id
		       movie_actor.role 			= role
		       movie_actor.save()
