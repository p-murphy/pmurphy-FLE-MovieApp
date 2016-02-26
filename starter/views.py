import json
import logging
import os
from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from utils import read_rotten_tomato_json, build_autocomplete_list


source_location = 'starter/more_movies.json'  # Option to switch json source.


def landing_page(request):
	return render(request, 'starter/landing_page.html')

def index(request):
	"""
	Read directly from JSON file, parse data to dict, and pass to index.html.
	"""
	try:  # Open JSON source. Log and redirect on failure.
		json_data = open(os.path.join(settings.MEDIA_ROOT, source_location))
	except IOError:
		logging.basicConfig(level=logging.INFO, 
			filename='myserver.log',
			format='%(asctime)s %(message)s')
		logging.info("- IOError opening movies.json in views.py/index")
		return render(request, "starter/404.html")
	else:
		with json_data:
			data = dict(json.load(json_data))
			json_data.close()

	movies = read_rotten_tomato_json(data)  # Build dict containing parsed movie data.
	movie_titles_list = build_autocomplete_list(movies)  # Build list to populate Search autocomplete.

	paginator = Paginator(movies, 10)  # Display results in pages, 10 per page.
	page = request.GET.get('page')
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)

	return render(request, 'starter/index.html', 
		{'data' : data, 'movie_titles_list' : movie_titles_list})


def details(request, movie_id):
	"""
	Read directly from JSON file, parse data to dict, and pass to details.html.
	"""
	try:  # Open JSON source. Log and redirect on failure.
		json_data = open(os.path.join(settings.MEDIA_ROOT, source_location))
	except IOError:
		logging.basicConfig(level=logging.INFO, 
			filename='myserver.log',
			format='%(asctime)s %(message)s')
		logging.info("- IOError opening movies.json in views.py/index")
		return render(request, "starter/404.html")
	else:
		with json_data:
			data = dict(json.load(json_data))
			json_data.close()

	movies = read_rotten_tomato_json(data)  # Build dict containing parsed movie data.
	movie_titles_list = build_autocomplete_list(movies)  # Build list to populate Search autocomplete.

	movie = None
	for movie_data in movies:
		if movie_data['id'] == movie_id:
			movie = movie_data  # Locate the movie data we are looking for.

	if movie is None:  # Ensure movie exists and is found. Log and redirect if not.
		logging.basicConfig(level=logging.INFO, 
					   filename='myserver.log',
					   format='%(asctime)s %(message)s')
		logging.info("- Movie object is null in views.py/details")
		return render(request, "starter/404.html", {'movie_titles_list' : movie_titles_list})

	release_theater = datetime.strptime(movie['release_theater'], "%Y-%m-%d")  # Make date pretty.

	return render(request, 'starter/details.html', 
		{'movie' : movie, 'release_theater' : release_theater,
		 'movie_titles_list' : movie_titles_list})


def search(request):
	"""
	Read user input from Search form in navigation bar defined in base.html.
	Use input to mimic Details results for now.
	"""
	movie_id = request.POST['idinput']  # For finding movie by id.
	movie_title = request.POST['titleinput']  # For ensuring name entered is not malformed.
	movie_title = movie_title.strip()  # Clean possible trailing and leading whitespace.

	try:  # Open JSON source. Log and redirect on failure.
		json_data = open(os.path.join(settings.MEDIA_ROOT, source_location))
	except IOError:
		logging.basicConfig(level=logging.INFO, 
			filename='myserver.log',
			format='%(asctime)s %(message)s')
		logging.info("- IOError opening movies.json in views.py/index")
		return render(request, "starter/404.html")
	else:
		with json_data:
			data = dict(json.load(json_data))
			json_data.close()

	movies = read_rotten_tomato_json(data)  # Build dict containing parsed movie data.
	movie_titles_list = build_autocomplete_list(movies)  # Build list to populate Search autocomplete.

	movie = None
	for movie_data in movies:
		if movie_data['title'] == movie_title:
			movie = movie_data  # Locate the movie data we are looking for, by title.

	if movie is None:  # Ensure movie title exists and is found. Log and redirect if not.
		logging.basicConfig(level=logging.INFO, 
    	               filename='myserver.log',
    	               format='%(asctime)s %(message)s')
		logging.info("- Movie object is null in views.py/details")
		return render(request, "starter/404.html", {'movie_titles_list' : movie_titles_list})

	movie = None
	for movie_data in movies:
		if movie_data['id'] == movie_id:
			movie = movie_data  # Locate the movie data we are looking for, by id.

	if movie is None:  # Ensure moviid id exists and is found. Log and redirect if not.
		logging.basicConfig(level=logging.INFO, 
					   filename='myserver.log',
					   format='%(asctime)s %(message)s')
		logging.info("- Movie object is null in views.py/details")
		return render(request, "starter/404.html", {'movie_titles_list' : movie_titles_list})

	release_theater = datetime.strptime(movie['release_theater'], "%Y-%m-%d")  # Make date pretty.

	return render(request, 'starter/details.html', 
		{'movie' : movie, 'release_theater' : release_theater,
		 'movie_titles_list' : movie_titles_list})


def about(request):
	"""
	Return simple About page.
	"""
	try:  # Open JSON source. Log and redirect on failure.
		json_data = open(os.path.join(settings.MEDIA_ROOT, source_location))
	except IOError:
		logging.basicConfig(level=logging.INFO, 
			filename='myserver.log',
			format='%(asctime)s %(message)s')
		logging.info("- IOError opening movies.json in views.py/index")
		return render(request, "starter/404.html")
	else:
		with json_data:
			data = dict(json.load(json_data))
			json_data.close()

	movies = read_rotten_tomato_json(data)  # Build dict containing parsed movie data.
	movie_titles_list = build_autocomplete_list(movies)  # Build list to populate Search autocomplete.

	return render(request, 'starter/about.html', {'movie_titles_list' : movie_titles_list})