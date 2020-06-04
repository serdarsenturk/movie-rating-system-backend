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
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=True, default='')
	gender = models.CharField(
		max_length=2,
		choices=GENDER_CHOISES,
		default = MALE,
	)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Review(models.Model):
    	review = models.CharField(max_length=200)

class Score(models.Model):
    	movieScore = models.CharField(max_length=200)

class Award(models.Model):
    	award = models.CharField(max_length=200)


class Movie(models.Model):
	name = models.CharField(max_length=200, blank=True, default='')
	genre = models.ManyToManyField(Genre)
	releasedYear = models.CharField(max_length=200, blank=True, default='')
	topic = models.CharField(max_length=200, blank=True, default='')
	actors = models.ManyToManyField(Actor)
	timeLength = models.CharField(max_length=200, blank=True, default='')
	budget = models.CharField(max_length=200, blank=True, default='')
	reviews = models.ManyToManyField(Review)
	score = models.ManyToManyField(Score)
	awards = models.ManyToManyField(Award)

	class Meta:
		ordering = ['name']
	
	def __str__(self):
    		return self.name

