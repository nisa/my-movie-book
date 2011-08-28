from django.contrib.auth.decorators import login_required
from django import forms
from forms import MovieForm
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from mysite.movies.models import Movie
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

#home page view
def home_page(request):
	return render_to_response("templates/home.html",context_instance=RequestContext(request))

#registration form for a new user
def register(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		new_user = form.save()
		return redirect(reverse("mysite.movies.views.signup_next"))
		
	return render_to_response("registration/register.html",{'form': form,},context_instance=RequestContext(request))
	    
# movie listing page for a logged in user    
@login_required
def movies_list(request):
      user = request.user
      movies_list = user.movie_set.all()
      movies_list = movies_list.order_by("-date_of_watching")
      paginator = Paginator(movies_list, 2)
      try: page = int(request.GET.get("page", '1'))
      except ValueError: page = 1
      try:
        movies_list = paginator.page(page)
      except (InvalidPage, EmptyPage):
        movies_list = paginator.page(paginator.num_pages)
      return direct_to_template(request, "templates/movies_list.html", {'movies_list': movies_list, 'user':user,}) 

# add movie form. Allows user to add a new movie
@login_required
def add_movie(request):
	if request.method == 'POST':
		form = MovieForm(request.POST)
		if form.is_valid():
			new_movie = form.save(commit=False)
			new_movie.user_id = request.user.id
			new_movie.save()
			request.user.message_set.create(message="Movie Added !!!")
			return redirect("movies_list")
	else:
		form = MovieForm()
	return direct_to_template(request, "templates/add_movie.html", {'form' : form,})
	
# delete a record and displays a message.
@login_required		
def delete_movie(request,pk=None):
	Movie.objects.get(pk=pk).delete()
	request.user.message_set.create(message="Record DELETED !!!")
	return redirect("movies_list")	

#user message after sign up 		
def signup_next(request):
	return direct_to_template(request, "registration/sign-up-next.html") 