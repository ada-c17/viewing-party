# ------------- WAVE 1 --------------------

import re
import string
from venv import create
from xml.dom import IndexSizeErr



def create_movie(title, genre, rating):
    movies = {}

    if title != None and genre != None and rating != None:
            movies.update({"title": title })
            movies.update({"genre": genre})
            movies.update({"rating": float(rating) })
    else:
        return None
    
    return movies

def add_to_watched(user_data, movies):
    
    user_data["watched"].append(movies)

    return user_data


def add_to_watchlist(user_data, movies):

    user_data["watchlist"].append(movies)

    return user_data

#adds movie to watched list
def watch_movie (user_data, movie_to_watch):
    
        for movie in user_data["watchlist"]:
            if movie["title"] == movie_to_watch:
                user_data["watched"].append(movie)
                user_data["watchlist"].remove(movie)
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    all_watched_ratings = []
    for movie in user_data["watched"]:
        all_watched_ratings.append(movie["rating"])

    if len(all_watched_ratings) > 0:
        return sum(all_watched_ratings) / len(all_watched_ratings)
    else:
        return 0

#genre is a string
def get_most_watched_genre(user_data):

    if user_data["watched"] != []:
        try:

            most_watched = {}
            description = []
            for movie in user_data["watched"]:
                if movie['genre']:
                    description.append(movie['genre'])
            for genre in description:
                if genre in most_watched:
                    most_watched[genre] += 1
                else:
                    most_watched[genre] = 1
            most_popular = max(most_watched.values())
            for keys, values in most_watched.items():
                if values == most_popular:
                    return keys
                return user_data
        except None:
            return  None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    unique_movies = []
    for movie in user_data["watched"]:
        watched_flag = False
        for friend in user_data["friends"]:
            if watched_flag:
                break
            for friend_movie in friend["watched"]:
                if movie == friend_movie:
                    watched_flag = True
        if not watched_flag:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    unique_movies = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            watched_flag = False

            for movie in user_data["watched"]:
                
                if movie == friend_movie:
                    watched_flag = True
            
            if not watched_flag and friend_movie not in unique_movies:
                unique_movies.append(friend_movie)

    return unique_movies

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
    recommendations = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommended_movies = []

    for movie in user_data["favorites"]:
        watched_flag = False
        for friend in user_data["friends"]:
            if watched_flag:
                break
            for friend_movie in friend["watched"]:
                if movie == friend_movie:
                    watched_flag = True
        if not watched_flag:
            recommended_movies.append(movie)
    return recommended_movies

    