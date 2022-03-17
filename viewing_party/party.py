# ------------- WAVE 1 --------------------

updated_data = {}

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    updated_data["watched"]= [movie]
    return updated_data


def add_to_watchlist(user_data, movie):
    updated_data["watchlist"]= [movie]
    return updated_data

def watch_movie(user_data, movie):
    updated_data["watched"] = user_data["watchlist"]
    return updated_data
    


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

