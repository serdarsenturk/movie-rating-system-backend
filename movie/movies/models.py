from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=200, blank=True, default='')
	genre = models.CharField(max_length=200, blank=True, default='')
	name = models.CharField(max_length=200, blank=True, default='')
	topic = models.CharField(max_length=200, blank=True, default='')
	actors = models.CharField(max_length=200, blank=True, default='')
	name = models.CharField(max_length=200, blank=True, default='')
	name = models.CharField(max_length=200, blank=True, default='')
	comment = models.CharField(max_length=200, blank=True, default='')
	name = models.CharField(max_length=200, blank=True, default='')
	awards = models.CharField(max_length=200, blank=True, default='')

class Serie(models.Model):
	name = models.CharField(max_length=200, blank=True, default='')
	serieCategory = models.CharField(max_length=200, blank=True, default='')	
	actors = models.CharField(max_length=200, blank=True, default='')
	name = models.CharField(max_length=200, blank=True, default='')

class Actor(models.Model):
	firstName = models.CharField(max_length=200, blank=True, default='')
	lastName = models.CharField(max_length=200, blank=True, default='')
	roles = models.CharField(max_length=200, blank=True, default='')