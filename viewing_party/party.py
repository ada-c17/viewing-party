# ------------- WAVE 1 --------------------
import pytest
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(movie_title, genre, rating):    

    if movie_title == None or genre == None or rating == None:
        return None

    new_movie = {}

    new_movie["title"] = movie_title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

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

def get_watched_avg_rating(user_data):

    count_rating = 0
    count_sum_rating = 0

    if not len(user_data["watched"]) == 0:
        for lists in user_data.values():
            for films in lists:
                count_sum_rating += films["rating"]
                count_rating += 1
        
        average = count_sum_rating/count_rating
    else:
        average = len(user_data["watched"])

    return average

def get_most_watched_genre(user_data):

    list_of_genre = []
    genre_dict = {}

    if not len(user_data["watched"]) == 0:
        for i in range(len(user_data["watched"])):
            list_of_genre.append(user_data["watched"][i]["genre"])

        for genre in list_of_genre:
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1

        max_value = 0
        popular_genre = ""

        for key,value in genre_dict.items():
            if value > max_value:
                max_value = value
                popular_genre = key
    else:
        popular_genre = None

    return popular_genre

get_most_watched_genre(user_data)
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

