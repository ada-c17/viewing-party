# ------------- WAVE 1 --------------------

from re import U
from typing import Counter


def create_movie(title, genre, rating):
    if not all([title, genre, rating]):
        return

    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(data, movie_title):
    item = None
    for movie in data['watchlist']:
        if movie['title'] == movie_title:
            item = movie
            break
    if item is None:
        return data

    data['watchlist'].remove(item)
    data['watched'].append(item)

    return data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(data):
    total_rating = 0
    for movie in data["watched"]:
        total_rating += movie["rating"]
    if len(data["watched"]) == 0:
        return 0
    return total_rating /len(data["watched"])

def get_most_watched_genre(data):
    
    counter = {}
    for movie in data["watched"]:
        if movie["genre"] not in counter:
            counter[movie["genre"]] = 0
        counter[movie["genre"]] += 1

    max_genre = None
    max_freq = 0
    for genre, frequency in counter.items():
        if frequency >= max_freq:
            max_genre = genre
            max_freq = frequency

    return max_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(data):
    unique = []
    friends_list_watched_movies = []

    for friend in data["friends"]:
        for movie in friend["watched"]:
            friends_list_watched_movies.append(movie['title'])

    for movie in data["watched"]:
        if movie["title"] not in friends_list_watched_movies:
            unique.append(movie)

    return unique

def get_friends_unique_watched(data):
    title_list = []
    for movie in data["watched"]:
        title_list.append(movie["title"])
    
    unique_watched_titles = set()
    unique_watched = []
    for friend in data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in title_list and movie["title"] not in unique_watched_titles:
                unique_watched.append(movie)
                unique_watched_titles.add(movie["title"])
                
                

    return unique_watched
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(data):
    user_subs = data['subscriptions']
    recommendations = []

    title_list = []
    for movie in data["watched"]:
        title_list.append(movie["title"])

    for friend_data in data["friends"]:
        for movie in friend_data["watched"]:
            sub = movie["host"]
            if sub in user_subs and movie["title"] not in title_list:
                recommendations.append(movie)
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(data):
    most_watched_genre = get_most_watched_genre(data)
    potential_rercs = []

    for friend in data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre and movie not in data['watched']:
                potential_rercs.append(movie)

    return potential_rercs


def get_rec_from_favorites(data):
    recommended_movies =[]
    favorites = data["favorites"]
    friends_watched = []

    for friend in data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in favorites:
        if movie not in friends_watched:
            recommended_movies.append(movie)
    return recommended_movies