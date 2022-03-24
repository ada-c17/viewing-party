# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """ creating movie dictionary and return movies of dictionary """

    # ditionary to store movies
    movies = {}

    # if any one of paramenters is None, function return None
    if title == None or genre == None or rating == None:
        return None

    # add movie into dictionary, if all paramenter is valid value or truthy
    elif title and genre and rating:
        
        movies["title"] = title
        movies["genre"] = genre
        movies["rating"] = rating
        return movies
    
    # Otherwise, return None.
    else:
        return None


def add_to_watched(user_data, movie):
    """ Adding movies into user data watched list and return user data"""

    # list to store watched movies
    watched_movies = []
    # add watched movies to a list
    watched_movies.append(movie)
    # add watched movies list into user data watched list
    user_data["watched"] = watched_movies
    return user_data


def add_to_watchlist(user_data, movie):
    """ Adding movies into user data watchlist and return user data """

    # list to store watchlist movies
    watchlist_movies = []
    # add watchlist movies to a list
    watchlist_movies.append(movie)
    # add watchlist movies list into user data watchlist
    user_data["watchlist"] = watchlist_movies
    return user_data


def watch_movie(user_data, title):
    """
    if the tile in the user's watchlist
        - remove movie from the watchlist
        - add movie to watched
        - return the user_data
    """
    # loop to get each movie in user watchlist for comparing with title
    for movie in user_data["watchlist"]:
        # if the title is in the user's movie watchlist 
        if title in movie["title"]:
            # add that movie into user's watched list
            user_data["watched"].append(movie)
            # remove that movie from user's watchlist
            user_data["watchlist"].remove(movie)
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


