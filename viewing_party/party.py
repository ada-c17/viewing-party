# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    new_movie = {"title" : movie_title , "genre" : genre , "rating" : rating }
    if movie_title == None:
        new_movie = None
        return new_movie
    elif genre == None:
        new_movie = None
        return new_movie
    elif rating == None:
        new_movie = None
        return new_movie
    return new_movie


def add_to_watched(user_data, movie):
    user_data = {
        "watched": []
    }
    user_data["watched"] += [movie]
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

