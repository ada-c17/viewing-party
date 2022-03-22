# ------------- WAVE 1 --------------------
import pytest
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(movie_title, genre, rating):    

    if movie_title == None or genre == None or rating == None:
        return None

    new_movie = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating
    }

    return new_movie

def add_to_watched(user_data, movie):

    list = user_data["watched"]
    list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    watchlist_list = user_data["watchlist"]
    watchlist_list.append(movie)

    return user_data


def watch_movie(user_data, movie):

    watchlist_list = user_data["watchlist"]
    watched_list = user_data["watched"]

    for film in watchlist_list:
        if film['title'] == movie:
            watched_list.append(film)
            watchlist_list.remove(film)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

