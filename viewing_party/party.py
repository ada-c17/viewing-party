
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    this function adds movie details to dictionary and returns movie details.
    if title is None, function returns None.
    '''
    new_movie = {
        "title": title,
        "genre":genre,
        "rating": rating
    }

    if title == None or genre == None or rating == None:
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
    # user_data["watched"] = movie
    user_data["watched"].append(movie)
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

