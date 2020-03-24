from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from movies.models import Movie
from movies.serializers import MovieSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, *args,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def movie_list(request):
	if request.method == 'GET':
		movies = Movie.objects.all()
		movie_serializer = MovieSerializer(movies, many=True)
		return JSONResponse(movie_serializer.data)

	elif request.method == 'POST':
		movie_data = JSONParser().parse(request)
		movie_serializer = MovieSerializer(data = movie_data)
		if movie_serializer.is_valid():
			movie_serializer.save()
			return JSONResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
		return JSONResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def movie_detail(request, pk):
	try:
		movie = Movie.objects.get(pk=pk)
	except Movie.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		movie_serializer = MovieSerializer(movie)
		return JSONResponse(movie_serializer.data)

	elif request.method == 'PUT':
		movie_data = JSONParser().parse(request)
		movie_serializer = MovieSerializer(movie, data = movie_data)
		if movie_serializer.is_valid():
			movie_serializer.save()
			return JSONResponse(movie_serializer.data)
		return JSONResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		movie.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)




