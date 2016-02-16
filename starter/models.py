from django.db import models

class Movie(models.Model):
	movie_id = models.IntegerField(max_length=200)
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class Actor(models.Model):
	movie = models.ForeignKey(Movie)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.first_name + " " + self.last_name
