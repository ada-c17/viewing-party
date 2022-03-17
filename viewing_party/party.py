# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title is None or genre is None or rating is None:
        return None
    movie_dict["title"] = title
    movie_dict["genre"] =  genre 
    movie_dict["rating"] =  rating
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"] =  [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] =  [movie]
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

