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


# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings_list = []
    watched_movies = user_data["watched"]
    for movie in watched_movies:
        new_rating = movie["rating"]
        ratings_list.append(new_rating)
    if ratings_list:
        return sum(ratings_list) / len(ratings_list)
    else:
        return 0


def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    watched_genres = [movie["genre"] for movie in watched_movies]
    most_watched_genre_dict = {}
    most_watched_genre = ""
    most_watched_counter = 0
    for genre in watched_genres:
        if genre in most_watched_genre_dict:
            most_watched_genre_dict[genre] += 1
        else:
            most_watched_genre_dict[genre] = 1
    for genre in most_watched_genre_dict:
        if most_watched_genre_dict[genre] > most_watched_counter:
            most_watched_genre = genre
            most_watched_counter = most_watched_genre_dict[genre]
    if most_watched_counter == 0:
        return None
    return most_watched_genre


# janes_data = {
#     "watched": [{
#         "title": "Grease",
#         "genre": "Fantasy",
#         "rating": 4.8},
#         {
#             "title": "Up",
#             "genre": "Action",
#             "rating": 4.0},
#         {
#         "title": "Sammy",
#         "genre": "Fantasy",
#         "rating": 4.0}]
# }
# print(get_most_watched_genre(janes_data))


# -----------------------------------------
# ------------- WAVE 3 -------∫-------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
