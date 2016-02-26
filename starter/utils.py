

def read_rotten_tomato_json(data):
	"""
	Read a json file passed in with *data*. 
	Read the file, strip and clean it,
	build new dicts, and pass them back to the caller.
	"""
	formatted_data = []
	id_list = []

	for movie in data['movies']:
		if movie['id'] not in id_list:
			item = {}
			item['id'] = movie['id']
			item['title'] = movie['title']
			item['year'] = movie.get('year', "")
			item['mpaa_rating'] = movie.get('mpaa_rating', "")
			item['runtime'] = movie.get('runtime', "")
			item['synopsis'] = movie.get('synopsis', "")

			if movie.get('release_dates', None) is not None:
				item['release_theater'] = movie['release_dates'].get('theater', "")
				item['release_dvd'] = movie['release_dates'].get('dvd', "")
			else:
				item['release_theater'] = ""
				item['release_dvd'] = ""

			item['critics_consensus'] = movie.get('critics_consensus', "")

			if movie.get('ratings', None) is not None:
				item['critics_rating'] = movie['ratings'].get('critics_rating', "")
				item['critics_score'] = movie['ratings'].get('critics_score', "")
				item['audience_rating'] = movie['ratings'].get('audience_rating', "")
				item['audience_score'] = movie['ratings'].get('audience_score', "")
			else:
				item['critics_rating'] = ""
				item['critics_score'] = ""
				item['audience_rating'] = ""
				item['audience_score'] = ""

			if movie.get('posters', None) is not None:
				item['thumbnail'] = movie['posters'].get('thumbnail', "")
				item['profile'] = movie['posters'].get('profile', "")
				item['detailed'] = movie['posters'].get('detailed', "")
				item['original'] = movie['posters'].get('original', "")
			else:
				item['thumbnail'] = ""
				item['profile'] = ""
				item['detailed'] = ""
				item['original'] = ""

			if movie.get('alternate_ids', None) is not None:
				item['imdb_id'] = movie['alternate_ids'].get('imdb', "")
			else:
				item['imdb_id'] = ""

			if movie.get('links', None) is not None:
				item['link_self'] = movie['links'].get('self', "")
				item['link_alternate'] = movie['links'].get('alternate', "")
				item['link_cast'] = movie['links'].get('cast', "")
				item['link_clips'] = movie['links'].get('clips', "")
				item['link_reviews'] = movie['links'].get('reviews', "")
				item['link_similar'] = movie['links'].get('similar', "")
			else:
				item['link_self'] = ""
				item['link_alternate'] = ""
				item['link_cast'] = ""
				item['link_clips'] = ""
				item['link_reviews'] = ""
				item['link_similar'] = ""

			if movie.get('links', None) is not None:
				abridged_cast = []
				for actor in movie['abridged_cast']:
					person = {}
					person['name'] = actor.get('name', "")
					person['id'] = actor.get('id', "")
					if actor.get('characters', None) is not None:
						characters = []
						for role in actor['characters']:
							characters.append(str(role))
						person['characters'] = characters
					abridged_cast.append(person)
				item['abridged_cast'] = abridged_cast
			else:
				item['abridged_cast'] = ""

			id_list.append(str(movie['id']))
			formatted_data.append(item)

	return formatted_data


def build_autocomplete_list(data):
	"""
	Take a parsed dict *data* built from read_rotten_tomato_json,
	and extract movie a movie_titles_list to be used for jQueryUI autocomplete feature.
	"""
	movie_titles_list = []
	for movie in data:
		item = {}
		item['key'] = str(movie['id'])
		item['value'] = str(movie['title'])
		movie_titles_list.append(item)

	return movie_titles_list
