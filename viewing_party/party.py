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

    list = user_data["watchlist"]
    list.append(movie)

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

