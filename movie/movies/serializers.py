from rest_framework import serializers
from movies.models import Movie, Genre, Actor, Review, Score

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('id', 'name', 'genre', 'releasedYear', 'topic', 'actors', 'timeLength', 'budget', 'reviews', 'score', 'awards')
		depth = 1

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actor
		fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Score
		fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		review = Review
		fields = '__all__'