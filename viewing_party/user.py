
from hashlib import new

from viewing_party.party import get_friends_unique_watched

from viewing_party.party import get_most_watched_genre

from .movie import Movie


class User():

	def __init__(self, watched = None, watchlist = None, favorites = None, friends = None, subscriptions = None):
		if watched == None:
			watched = []

		if watchlist == None:
			watchlist = []

		if favorites == None:
			favorites = []

		if friends == None:
			friends = []

		if subscriptions == None:
			subscriptions == []

		self.watched = watched
		self.watchlist = watchlist
		self.favorites = favorites
		self.friends = friends
		self.subscriptions = subscriptions

	def add_to_watchlist(self, movie):
		self.watchlist.append(movie)
		# return self.watchlist

	def watch_movie(self, title):
		new_watchlist = []

		for index in range(len(self.watchlist)):
			if title in self.watchlist[index].title:
				self.watched.append(self.watchlist[index])
			else:
				new_watchlist.append(self.watchlist[index])
		
		self.watchlist = new_watchlist

		# return self.watched
	
	def get_watched_average_rating(self):
		total = 0
		for movie in self.watched:
			total += movie.rating

		try:
			average = total/ len(self.watched)
		except ZeroDivisionError:
			return 0
		
		return average

	def get_most_watched_genre(self):
		if len(self.watched) == 0:
			return None

		genre_count = {}

		for movie in self.watched:
			if movie.genre not in genre_count:
				genre_count[movie.genre] = 1
			else:
				genre_count[movie.genre] += 1
		
		return max(genre_count, key = genre_count.get)

	def get_unique_watched(self):

		friends_watched_titles = []

		for friend in self.friends:
			for movie in friend.watched:
				friends_watched_titles.append(movie.title)

		unique_movies = []

		for movie in self.watched:
			if movie.title not in friends_watched_titles:
				unique_movies.append(movie)
		
		return unique_movies

	def get_friends_unique_watched(self):
		friend_watched_movies = []

		for friend in self.friends:
			for movie in friend.watched:
				friend_watched_movies.append(movie)

		user_watched_titles = []

		for movie in self.watched:
			user_watched_titles.append(movie.title)

		unique_movie = []

		for friend_movie in friend_watched_movies:
			if friend_movie.title not in user_watched_titles and friend_movie not in unique_movie:
				unique_movie.append(friend_movie)
		
		return unique_movie

	def get_recs(self):
		friends_unique_watched_movies = get_friends_unique_watched()

		recommended_movies = []

		for movie in friends_unique_watched_movies:
			if movie.host in self.subscriptions:
				recommended_movies.append(movie)

		return recommended_movies
	
	def get_new_rec_by_genre(self):
		
		most_watched_genre = get_most_watched_genre()

		friends_unique_watched_movies = get_friends_unique_watched()

		recommended_movies = []

		for movie in friends_unique_watched_movies:
			if movie.genre == most_watched_genre:
				recommended_movies.append(movie)

		return recommended_movies

	
