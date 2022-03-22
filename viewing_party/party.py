# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass
    # using the parameters title, genre, and rating, create a dictionary called new_movie
    # with keys "title", "genre", and "rating"
    # and values that are equal to title, genre, rating

    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        new_movie = None

    return new_movie

def add_to_watched(user_data, movie):
    # this function should add the dictionary movie to user_data.
    # user_data is also a dictionary with one key, "watched"
    # the value of user_data["watched"] is a list of dictionaries (i.e., each movie),
    # each with keys "title", "genre", and "rating"

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

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

