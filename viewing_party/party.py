# ------------- WAVE 1 --------------------

from ast import And
from itertools import count
from site import USER_BASE
from typing import Counter
import copy # I want to import copy module to use deepcopy
'''I have choosen to use the deepcopy to ensure that I am not making
changes to orginal list that is passed through the functions.
For 3 of the functions in this wave, I am making changes to the new list.
However, as we know, if I simply do a shallow copy, it will also change the
orgiginal list since the elements in both the orginal list and new list
are referecing the same ID number. By createing a deepcopy, I can ensure that
as the function iterates  through the old list and make changes to the new list, 
the changes will only affect the new list.'''


def create_movie(title, genre, rating):
    new_movie = {}

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    if new_movie["title"] == None or\
        new_movie["genre"] == None or\
            new_movie["rating"] == None:
        return None     

    return new_movie

def add_to_watched(user_data, movie):
    watched_movie = copy.deepcopy(user_data)
    watched_movie["watched"].append(movie)
    return watched_movie

def add_to_watchlist(user_data, movie):
    watchlist_movie = copy.deepcopy(user_data)
    watchlist_movie["watchlist"].append(movie)
    return watchlist_movie

def watch_movie(user_data, movie_title):
    updated_movie = copy.deepcopy(user_data)
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"]:
            updated_movie["watched"].append(movie)
            updated_movie["watchlist"].remove(movie)
    return updated_movie




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    my_ratings_total = 0
    movie_len = len(user_data["watched"])
    if not user_data["watched"]:
        return 0
    
    for movies in user_data["watched"]:
        my_ratings_total += float(movies["rating"])
    
    rating_average = my_ratings_total / movie_len
    return rating_average

def get_most_watched_genre(user_data):
    genres = []
    popular_genre_count = 0
    most_popular_genre = ()
    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    for genre in genres:
        if not user_data["watched"]:
            return None
        if genres.count(genre) >= popular_genre_count:
            popular_genre_count = genres.count(genre)
            most_popular_genre = genre
            
        return most_popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    for movie in user_data["watched"]:
        if movie not in get_friends_movies(user_data):
            unique_movies.append(movie)
    return unique_movies

def get_friends_movies(user_data):
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie) # don't need
    return friends_movies

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    for movie in get_friends_movies(user_data):
        if movie not in user_data["watched"] and \
            movie not in friends_unique_list:
                friends_unique_list.append(movie) 
    return friends_unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_rec = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            genre_rec.append(movie)
    return genre_rec

def get_rec_from_favorites(user_data):
    fav_rec = []
    for movie in user_data["favorites"]:
        if movie not in get_friends_movies(user_data):
            fav_rec.append(movie)
    return fav_rec