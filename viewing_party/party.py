from doctest import ELLIPSIS
from pickle import NONE

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie = {"title" : title, "genre" : genre, "rating":rating }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for num_movies in range(len(user_data["watchlist"])):
        if user_data["watchlist"][num_movies]["title"] == title: 
            movie = user_data["watchlist"].pop(num_movies)
            user_data["watched"].append(movie)
            break        
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    addition = 0
    if len(user_data["watched"])>=1: 
        for num_movies in range(0,len(user_data["watched"])):
            addition += user_data["watched"][num_movies]["rating"]
        average = addition/ len(user_data["watched"])
    else:
        average = 0.0
    return average


def get_most_watched_genre(user_data):
    genre_dict = {}
    
    
    for movie in user_data["watched"]:
        genre_var = movie["genre"]
        if genre_var in genre_dict:
            genre_dict[genre_var] +=1
        else:
            genre_dict[genre_var] = 1   

    popular_genre = None
    counter_genre = 0
    for genre in genre_dict:
        if genre_dict[genre] > counter_genre:
            popular_genre = genre
            counter_genre = genre_dict[genre] 
            

    return popular_genre

        


    
        
        


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

