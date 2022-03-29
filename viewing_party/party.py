# ------------- WAVE 1 --------------------

from enum import unique
from logging.handlers import RotatingFileHandler
from re import L, U
import re
from tests.test_constants import MOVIE_TITLE_1, USER_DATA_2
import copy
import statistics


def create_movie(movie_title, genre, rating):
    if not movie_title or not genre or not rating:
        return None
    new_movie = {
        "title" : movie_title, 
        "genre": genre,
        "rating": rating }
    return new_movie

def add_to_watched(user_data, movie):
     user_data["watched"].append(movie)
     return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie_to_watch in user_data["watchlist"]:
        if movie_to_watch["title"] == title:
            user_data["watchlist"].remove(movie_to_watch)
            user_data["watched"].append(movie_to_watch)
    return user_data

def watched_movie(user_data, title):
    for movie_to_watch in user_data["watched"]:
        if movie_to_watch["title"] == movie_to_watch["title"]:
            user_data["watchlist"].remove(movie_to_watch)
            user_data["watched"].append(movie_to_watch)
    return user_data

def nonexistent_movie(user_data, title):
    for movie_to_watch in user_data["watched"]:
        if movie_to_watch["title"] != movie_to_watch["title"]:
            return None
    
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating_list= []
    # check_empty = []
    default_to_zero = 0
    if bool(user_data["watched"]) == False:
        avg_rating_list.append(default_to_zero)
        avg = sum(avg_rating_list)/len(avg_rating_list)
        return avg
    else:
        for movie in user_data["watched"]:
            avg_rating_list.append(movie["rating"])
            avg = sum(avg_rating_list)/len(avg_rating_list)
        return avg


def get_most_watched_genre(user_data):
    get_most_watched = []
    if bool(user_data["watched"]) == False:
        get_most_watched.append(None)
        popular_genre = statistics.mode(get_most_watched)
        return popular_genre
        
    else:
        for movie in user_data["watched"]:
            get_most_watched.append(movie["genre"])
            popular_genre = statistics.mode(get_most_watched)
        return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# get list of all friends movies(titles)
# check if each users movie is in list of movie(title)

def get_unique_watched(user_data):
    unique_list = []
    friends_titles= []

    for friends_data in user_data["friends"]:
        for friends_movie in friends_data["watched"]:
            friends_titles.append(friends_movie["title"])


    for movie in user_data["watched"]:
        if movie["title"] not in friends_titles:
            unique_list.append(movie)

    return unique_list

def get_friends_unique_watched(user_data):
    friends_movie_list =[]
    for friend_data in user_data["friends"]:
        for friends_movie in friend_data["watched"]:
            if friends_movie not in user_data["watched"] and friends_movie not in friends_movie_list:
                friends_movie_list.append(friends_movie)
    return friends_movie_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []

    unique_watch_list = get_friends_unique_watched(user_data)
    
    for user_sub in range(len(user_data["subscriptions"])):
        for sub in range(len(unique_watch_list)):
            if user_data["subscriptions"][user_sub] == unique_watch_list[sub]["host"]:
                recommendations.append(unique_watch_list[sub])


    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    
    mode_genre = get_most_watched_genre(user_data)
    new_recommendations = []
    rec_recommendations = get_friends_unique_watched(user_data)

    for user_movie in rec_recommendations:
        if rec_recommendations[rec_recommendations.index(user_movie)]["genre"] == mode_genre:
            new_recommendations.append(user_movie)

    return new_recommendations



def get_rec_from_favorites(user_data):
    rec_recommendations = []
    unique_watch_list = get_unique_watched(user_data)

    for user_movie in unique_watch_list:
        if user_movie in user_data["favorites"]:
            rec_recommendations.append(user_movie)

    return rec_recommendations




    #refactored code 

        # user_unique_list = []
    # friends_titles= []
    # friend_unique_list = []

    # for friends_data in user_data["friends"]:
    #     for friends_movie in friends_data["watched"]:
    #         friends_titles.append(friends_movie)


    # for movie in user_data["watched"]:
    #     user_unique_list.append(movie)

        
    # for movie in friends_titles:
    #     if movie not in user_unique_list:
    #         friend_unique_list.append(movie)
            

    # return friend_unique_list

    #     for friends_data in user_data["friends"]:
    #     for friends_movie in friends_data["watched"]:
    #         friends_titles.append(friends_movie["title"])


    # for movie in user_data["watched"]:
    #     if movie["title"] not in friends_titles:
    #         unique_list.append(movie)