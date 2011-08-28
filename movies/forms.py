from django.forms import ModelForm 
from movies.models import Movie

class MovieForm(ModelForm):
      class Meta:
            model = Movie
            exclude = ('user',)
           
