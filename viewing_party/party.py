# ------------- WAVE 1 --------------------

import pytest


def create_movie(title, genre, rating):
    new_movie_dict = {}
    new_movie_dict["title"] = title
    new_movie_dict["genre"] = genre
    new_movie_dict["rating"] = rating
    for value in new_movie_dict.values():
        if value == None:
            return None
    return new_movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            found_watched_movie = movie
            user_data["watched"].append(found_watched_movie)
            index = watchlist.index(movie)
            user_data["watchlist"].pop(index)
    return user_data


def get_watched_average_rating(user_data):
    pass


# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 -------∫-------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
