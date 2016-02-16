
import logging
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from starter.models import Movie
from utils import read_json, build_autocomplete_list


def landing_page(request):
    return render(request, 'starter/landing_page.html')


def index(request):
	"""
	Read directly from JSON file, parse data to dict, and pass to index.html.
	"""
	data = read_json('starter/movies.json')  # Build dict containing parsed movie data.

	movie_titles_list = build_autocomplete_list(data)  # Build list to populate Search autocomplete.

	return render(request, 'starter/index.html', 
		{'data' : data, 'movie_titles_list' : movie_titles_list})


def details(request, movie_id):
	"""
	Read directly from JSON file, parse data to dict.
	Also read data from model to suppliment JSON data, and pass both to details.html.
	"""
	data = read_json('starter/movies.json')  # Build dict containing parsed movie data.

	movie_titles_list = build_autocomplete_list(data)  # Build list to populate Search autocomplete.

	movie = None
	for movie_data in data['movies']:
		if movie_data['id'] == movie_id:
			movie = movie_data  # Locate the movie data we are looking for.

	if movie is None:  # Ensure movie exists and is found. Log and redirect if not.
		logging.basicConfig(level=logging.INFO, 
    	               filename='myserver.log',
    	               format='%(asctime)s %(message)s')
		logging.info("- Movie object is null in views.py/details")
		return render(request, "starter/404.html", {'movie_titles_list' : movie_titles_list})

	actors = get_object_or_404(Movie, movie_id=movie_id).actor_set.all()
	actors_list = ', '.join([act.first_name + " " + act.last_name for act in actors])  # Build actors list from model.

	release_date = datetime.strptime(movie['release_dates']['theater'], "%Y-%m-%d")  # Make date pretty.

	return render(request, 'starter/details.html', 
		{'movie' : movie, 'release_date' : release_date,
		 'movie_titles_list' : movie_titles_list, 'actors_list' : actors})


def search(request):
	"""
	Read user input from Search form in navigation bar defined in base.html.
	Use input to mimic Details results for now.
	"""
	user_input = request.POST['userinput']

	data = read_json('starter/movies.json')  # Build dict containing parsed movie data.

	movie_titles_list = build_autocomplete_list(data)  # Build list to populate Search autocomplete.

	movie = None
	for movie_data in data['movies']:
		if movie_data['title'] == user_input:
			movie = movie_data  # Locate the movie data we are looking for.

	if movie is None:  # Ensure movie exists and is found. Log and redirect if not.
		logging.basicConfig(level=logging.INFO, 
    	               filename='myserver.log',
    	               format='%(asctime)s %(message)s')
		logging.info("- Movie object is null in views.py/details")
		return render(request, "starter/404.html", {'movie_titles_list' : movie_titles_list})

	release_date = datetime.strptime(movie['release_dates']['theater'], "%Y-%m-%d")  # Make date pretty.

	actors = get_object_or_404(Movie, movie_id=movie['id']).actor_set.all()
	actors_list = ', '.join([act.first_name + " " + act.last_name for act in actors])  # Build actors list from model.

	return render(request, 'starter/details.html', 
		{'movie' : movie, 'release_date' : release_date,
		 'movie_titles_list' : movie_titles_list, 'actors_list' : actors})


def about(request):
	"""
	Return simple About page.
	"""
	data = read_json('starter/movies.json')  # Build dict containing parsed movie data.

	movie_titles_list = build_autocomplete_list(data)  # Build list to populate Search autocomplete.

	return render(request, 'starter/about.html', {'movie_titles_list' : movie_titles_list})