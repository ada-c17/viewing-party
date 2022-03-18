# ------------- WAVE 1 --------------------
    
def create_movie(title, genre, rating):
    new_movie = {"title" : title, "genre" : genre, "rating" : rating}
    if new_movie["title"] == None or new_movie["genre"] == None or new_movie["rating"] == None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {
        "watched": [movie]
    }
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data


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