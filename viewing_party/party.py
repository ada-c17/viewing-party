
from collections import Counter
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            add_to_watched(user_data, title)
    return user_data
        
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    rating_list = []
    for movie in watched_movies:
       rating_list.append(movie["rating"])
    if len(rating_list) == 0:
        avg_rating = 0
    else:
        avg_rating = sum(rating_list)/len(rating_list)
    return avg_rating

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    genre_list = []
    for movie in watched_movies:
       genre_list.append(movie["genre"])
    if len(genre_list) == 0:
        return None
    most_watched_genre_dict = dict(Counter(genre_list))
    max_val = max(most_watched_genre_dict.values())
    most_watched_genre = ([key for key, val in most_watched_genre_dict.items() if val == max_val])
    return ''.join(most_watched_genre)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

