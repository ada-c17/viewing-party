# ------------- WAVE 1 --------------------

from ast import And
from itertools import count
from site import USER_BASE
from typing import Counter


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
    watched_movie = user_data
    watched_movie["watched"].append(movie)
    # print(user_data)
    return watched_movie

def add_to_watchlist(user_data, movie):
    watchlist_movie = user_data
    watchlist_movie["watchlist"].append(movie)
    return watchlist_movie

def watch_movie(user_data, movie_title):
    updated_movie = user_data
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"]:
            updated_movie["watched"].append(movie)
            updated_movie["watchlist"].remove(movie)
    return updated_movie




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = 0
    if not user_data["watched"]:
        return 0

    for movies in user_data["watched"]:
        rating_total += float(movies["rating"])
    
    movie_len = len(user_data["watched"])
    rating_average = rating_total / movie_len
    return rating_average

def get_most_watched_genre(user_data):
    genres = []
    popular_genre_count = 0
    popular_genre = ()
    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    for genre in genres:
        if not user_data["watched"]:
            return None
        if genres.count(genre) >= popular_genre_count:
            popular_genre_count = genres.count(genre)
            popular_genre = genre
            
        return popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    for movie in get_my_movies(user_data):
        if movie not in get_friends_movies(user_data):
            unique_movies.append(movie)
    return unique_movies

def get_my_movies(user_data):
    return user_data["watched"]
    # my_movies = []
    # for movie in user_data["watched"]:
    #     my_movies.append(movie) # don't need
    # return my_movies

def get_friends_movies(user_data):
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie) # don't need
    return friends_movies

# friends_unique_watched = get_friends_unique_watched(user_data)

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    for movie in get_friends_movies(user_data):
        if movie not in get_my_movies(user_data) and \
            movie not in friends_unique_list:
                friends_unique_list.append(movie) 
    return list(friends_unique_list)

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