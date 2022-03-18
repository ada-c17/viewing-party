from test_constants import *

def create_movie(title, genre, rating):
    # If title, genre, or rating are "None", return None
    if title == None or genre == None or rating == None:
        movie = None
    # Otherwise, create movie with title, genre, and rating
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    
    return movie

def add_to_watched(user_data, movie):
    # Add movie to user's watched
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # Add movie to user's watchlist
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # Move movie from user's watchlist to watched
    movie = user_data["watchlist"][0]
    user_data["watched"].append(movie)
    user_data["watchlist"].remove(movie)
    return user_data

# test data
janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }

movie = create_movie(MOVIE_TITLE_1, GENRE_1, RATING_1)
updated_data = add_to_watched(janes_data, movie)
updated_data = watch_movie(janes_data, MOVIE_TITLE_1)

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

