from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=200, blank=True, default='')
	movieCategory = models.CharField(max_length=200, blank=True, default='')

	class Meta:
		ordering = ('name', )