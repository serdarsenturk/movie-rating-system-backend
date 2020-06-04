from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('name', 'genre', 'releasedYear', 'topic', 'actors', 'timeLength', 'budget', 'reviews', 'score', 'awards')

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		field = (
			'name',
		)
class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		field = (
			'created',
			'name',
			'gender'
		)

class MovieScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		field = (
			'movie',
			'score',
			'scoreDate'
		)