
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
    '''
    this function adds movie data in the form of a dictionary
    to a dictionary of user_data, where the key is watched and
    the values are a list of dictionaries of movies the user has watched
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    this function adds movie data in the form of a dictionary
    to a dictionary of user_data, where the key is watchlist and
    the values are a list of dictionaries of movies the user has queued to watch
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    this function will move a movie from watchlist to watched
    '''
    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].pop()
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

