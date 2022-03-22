# ------------- WAVE 1 --------------------

from curses import keyname
from xml.sax.handler import EntityResolver

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1, USER_DATA_2


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

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

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

def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]: # for movie in the watched list
        for category, item in movie.items():
            if category == "rating":
                ratings.append(item)   
    average_rating = ((sum(ratings))/(len(ratings)))
    return average_rating

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------