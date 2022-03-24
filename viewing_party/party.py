# ------------- WAVE 1 --------------------

from curses import keyname
from lib2to3.pgen2.tokenize import generate_tokens
from operator import itemgetter
from xml.sax.handler import EntityResolver

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1, USER_DATA_2

# adds movie data as item in movie dictionary
def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else: 
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
    }

    return movie

# adds movie to watched list
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

# adds movie to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

# moves watchlist movie to watched list
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        for category, item in movie.items():
            if category == "title" and item == title:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# gets average rating of movies for user
def get_watched_avg_rating(user_data):
    ratings = []
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]: 
            for category, item in movie.items():
                if category == "rating":
                    ratings.append(item)   
        average_rating = ((sum(ratings))/(len(ratings)))
    else:
        average_rating = 0
    return average_rating

# returns most watched genre in user's movies
def get_most_watched_genre(user_data):
    genres = {}
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]: 
            for category, item in movie.items():
                if category == "genre":
                    if item not in genres:
                        genres[item] = 0
                    else:
                        genres[item] += 1
        popular_genre = (max(genres, key=genres.get))
        return popular_genre

    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# returns unique movie from user's movies
def get_unique_watched(user_data):
    unique_watched = []
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    friend_movies = []
    for friend in friends: # loops through friend 0 and friend 1
        friend_movies += friend["watched"] #assigns list
    for user_movie in user_watched: #gets the first user movie
        if user_movie not in friend_movies:
                if user_movie not in unique_watched:
                    unique_watched.append(user_movie)

    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------