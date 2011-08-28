from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
		title = models.CharField(max_length=100)
		director = models.CharField(max_length=100)
		date_of_release = models.DateField()
		date_of_watching = models.DateField()
		user = models.ForeignKey(User)