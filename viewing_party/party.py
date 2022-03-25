# ------------- WAVE 1 --------------------

from cmath import rect
from time import monotonic


def create_movie(title, genre, rating):
    movie_dict = {}

    if title and genre and rating:
        movie_dict['title'] = title 
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for movie_dicts in user_data['watchlist']:
        if movie_dicts['title'] == movie:
            user_data['watched'].append(movie_dicts)
            user_data['watchlist'].remove(movie_dicts)    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_total = 0
    watch_counter = 0
    
    for movie_dicts in user_data['watched']:
        rating_total += movie_dicts['rating']
        watch_counter += 1

    if rating_total > 0:
        avg_rating = rating_total/watch_counter
    else:
        avg_rating = 0
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []

    for movie_dicts in user_data['watched']:
        genre_list.append(movie_dicts['genre'])
    if genre_list:
        return max(set(genre_list), key = genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_movies = user_data['watched']
    friends_movies = []
    user_unique_movies = []

    for movie_dicts in user_data['friends']:
        for movie in movie_dicts['watched']:
            friends_movies.append(movie)

    for user_movie in user_movies:
        if user_movie not in friends_movies and user_movie not in user_unique_movies:
            user_unique_movies.append(user_movie) 
    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data['watched']
    friends_movies = []
    friends_unique_movies = []

    for movie_dicts in user_data['friends']:
        for movie in movie_dicts['watched']:
            friends_movies.append(movie)

    for movie_dicts in friends_movies:
        if movie_dicts not in user_movies and movie_dicts not in friends_unique_movies:
            friends_unique_movies.append(movie_dicts) 
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_subscriptions = user_data['subscriptions']
    user_recommendations = []
    friends_watched = []

    for movie_dicts in user_data['friends']:
        for movie in movie_dicts['watched']:
            friends_watched.append(movie)

    for movie_dicts in friends_watched:
        if movie_dicts['host'] in user_subscriptions and movie_dicts not in user_data['watched'] and movie_dicts not in user_recommendations:
            user_recommendations.append(movie_dicts)

    return user_recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_most_watched = get_most_watched_genre(user_data)
    friends_watched = []
    most_genre_recommendations = []

    for movie_dicts in user_data['friends']:
        for movie in movie_dicts['watched']:
            friends_watched.append(movie)

    for movie_dicts in friends_watched:
        if movie_dicts not in user_data['watched'] and movie_dicts['genre'] == genre_most_watched:
            most_genre_recommendations.append(movie_dicts)

    return most_genre_recommendations

def get_rec_from_favorites(user_data):
    user_favorites = user_data['favorites']
    friends_watched = []
    rec_from_favorites = []

    for movie_dicts in user_data['friends']:
        for movie in movie_dicts['watched']:
            friends_watched.append(movie)
    
    for movie_dicts in user_favorites:
        if movie_dicts not in friends_watched:
            rec_from_favorites.append(movie_dicts)

    return rec_from_favorites
