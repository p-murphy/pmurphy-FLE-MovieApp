import json
import os
import logging
from django.shortcuts import render
from django.conf import settings


def read_json(filename):
	"""
	Read a json file located at *filename*. 
	Try opening it. If failed, write to log and
	redirect to starter/404.html. Else pass parsed
	json dictionary back to caller.
	"""
	try:
		json_data = open(os.path.join(settings.MEDIA_ROOT, filename))
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
		return data


def build_autocomplete_list(data):
	"""
	Take a parsed dict *data* built from read_json, and extract movie a movie_titles_list
	to be used for jQueryUI autocomplete feature.
	"""
	movie_titles_list = []
	for movie_data in data['movies']:
		movie_titles_list.append(str(movie_data['title']))

	return movie_titles_list
