# ------------- WAVE 1 --------------------

import re
import string
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
    
    user_data = {
        "watched" : [movies]
    }
    return user_data


def add_to_watchlist(user_data, movies):
    user_data = {
        "watchlist" : [movies]
    }
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
    total_ratings = []
    if user_data["watched"] != []:
        try:
            for movie in user_data["watched"]:
                total_ratings.append(movie['rating'])

            number_of_ratings = len(total_ratings)
            average_rating = sum(total_ratings)/int(number_of_ratings)
        except ZeroDivisionError:
            average_rating = 0
    else:
        average_rating = 0

    return average_rating

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

def create_friends_dictionary(user_data):
    friends_movies = {}
    friends_movies[1] = user_data["friends"][0]
    friends_movies[2] = user_data["friends"][1]
    return friends_movies

def get_unique_watched(user_data):
    friends_movies = create_friends_dictionary(user_data)
    users_unique_movies = []

    for title in user_data["watched"]:
        if title not in friends_movies[1]["watched"] and title not in friends_movies[2]["watched"]:
            users_unique_movies.append(title)
    return users_unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friends_movies = create_friends_dictionary(user_data)
    
    for movie in friends_movies[1]["watched"]:
        if movie not in user_data["watched"]:
            if movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    for friend_movies in friends_movies[2]["watched"]:
        if friend_movies not in user_data["watched"]:
            if friend_movies not in friends_unique_movies:
                friends_unique_movies.append(friend_movies)
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []
    friends_movies = create_friends_dictionary(user_data)

    for movie in friends_movies[1]["watched"]:
        if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)
        for movie in friends_movies[2]["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommendations = []
    friends_movies = create_friends_dictionary(user_data)

    if user_data["watched"] != []:
        if friends_movies[1]["watched"] != []:
            for movie in friends_movies[1]["watched"]:
                if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                    recommendations.append(movie)
            if friends_movies[2]["watched"] != []:
                for movie in friends_movies[2]["watched"]:
                    if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                        recommendations.append(movie)
            for rec in recommendations:
                if rec["genre"] not in user_data["watched"][0]["genre"]:
                    recommendations.remove(rec)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    friends_movies = create_friends_dictionary(user_data)

    for movie in user_data["watched"]:
        if user_data["favorites"] != []:
            if friends_movies[1]["watched"] != [] and friends_movies[2]["watched"] != []:
                if movie in user_data["favorites"] and movie not in friends_movies[1]["watched"] and movie not in friends_movies[2]["watched"] and movie not in recommendations:
                    recommendations.append(movie)
    return recommendations

    