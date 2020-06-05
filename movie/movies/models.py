from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=200)
	class Meta:
		ordering = ['name']
	def __str__(self):
		return self.name

class Actor(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOISES = (
		(MALE, 'Male'),
		(FEMALE,'Female')
	)
	name = models.TextField(max_length=200, blank=True, default='')
	surname = models.TextField(max_length=200, blank=True, default='')
	gender = models.CharField(
		max_length=2,
		choices=GENDER_CHOISES,
		default = MALE,
	)

	class Meta:
		ordering = ('name',)

class Review(models.Model):
    	review = models.CharField(max_length=200)

class Score(models.Model):
    	movieScore = models.IntegerField(max_length=200)

class Award(models.Model):
    	award = models.CharField(max_length=200)


class Movie(models.Model):
	name = models.CharField(max_length=200, blank=True, default='')
	genre = models.ManyToManyField(Genre)
	releasedYear = models.IntegerField(max_length=200, blank=True, default='')
	topic = models.CharField(max_length=200, blank=True, default='')
	actors = models.ManyToManyField(Actor, related_name='movies')
	timeLength = models.CharField(max_length=200, blank=True, default='')
	budget = models.IntegerField(max_length=200, blank=True, default='')
	reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
	score = models.ForeignKey(Score, on_delete=models.CASCADE)
	awards = models.ManyToManyField(Award)

	class Meta:
		ordering = ['name']