from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=200)
	movieCategory = serializers.CharField(max_length=200)


	def create(self, validated_data):
		return Movie.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.movieCategory = validated_data.get('movieCategory', instance.movieCategory)
		instance.save()
		return instance