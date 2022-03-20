
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

def get_watched_avg_rating(user_data):
    '''
    this function calculates the average rating of the
    movies in the watched list
    '''
    num_movies_watched = 0
    rating_sum = 0
    for lst_name, lst_contents in user_data.items():
        num_movies_watched += len(lst_contents)
        for movie in lst_contents:
            rating_sum += movie["rating"]

    if num_movies_watched == 0:
        average_rating = 0
    else:
        average_rating = rating_sum/num_movies_watched
        
    return average_rating


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

