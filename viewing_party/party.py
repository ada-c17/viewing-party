# ------------- WAVE 1 --------------------

from imp import new_module
from turtle import up


def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
        return None
    new_movie['title'] = title
    new_movie['genre'] = genre
    new_movie['rating'] = rating 
    return new_movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    for film in watchlist:
        if film['title'] == movie_title:
            watchlist.remove(film)
            watched.append(film) 
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched = user_data['watched']
    rating_sum = 0

    for movie in watched:
        rating_sum  += movie['rating']
    
    rating_avg = rating_sum / len(watched)
    return rating_avg


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------