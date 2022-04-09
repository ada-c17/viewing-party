# ------------- WAVE 1 --------------------

from enum import unique
from xml.sax.handler import feature_namespace_prefixes


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        movie_data = None

    else:
        movie_data = {
            'title': title,
            'genre': genre,
            'rating': rating
            }
            
    return movie_data


def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    try:
        total = 0
        for movie in user_data["watched"]:
            total += movie['rating']
        average = total / len(user_data["watched"])

    except ZeroDivisionError:
        average = 0.0

    return average


def get_most_watched_genre(user_data):
    if user_data["watched"]:
        genre_list = [movie["genre"] for movie in user_data["watched"]]
        most_popular_genre = max(genre_list, key = genre_list.count)
    else:
        most_popular_genre = None

    return most_popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_watched_movie_titles(user_data):
    friends_watched_movie_titles = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_watched_movie_titles:
                friends_watched_movie_titles.add(movie["title"])
    
    return friends_watched_movie_titles

def get_user_watched_movie_titles(user_data):
    user_watched_movie_titles = set()

    for movie in user_data["watched"]:
        if movie["title"] not in user_watched_movie_titles:
            user_watched_movie_titles.add(movie["title"])
    
    return user_watched_movie_titles

def get_unique_watched(user_data):
    '''
    Determines which movies the user has watched, but none of their friends have watched.

    Parameter:
    user_data (dict): Movies the user has watched.

    Returns:
    unique_watched_movies (list): List of dictionaries representing the movies the user has watched and their friends have not watched.
    '''
    unique_watched = []

    friends_watched_movie_titles = get_friends_watched_movie_titles(user_data)
    # user_watched_movie_titles = get_user_watched_movie_titles(user_data)

    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_movie_titles and movie["title"] not in unique_watched:
            unique_watched.append(movie)
    
    return unique_watched
    

def get_friends_unique_watched(user_data):
    '''
    Determines which movies at least one of the user's friends have watched, but the user has not watched.
    
    Returns:
    (list): List of dictionaries that represents a list of movies.
    '''
    user_watched_movie_titles = get_user_watched_movie_titles(user_data)
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_movie_titles and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)  

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass


def get_rec_from_favorites(users_data):
    pass