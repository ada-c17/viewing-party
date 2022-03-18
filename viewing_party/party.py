

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # creating a dictionary that stores the variables passed into the function as the values
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # checks to make sure that the variables passed into the function are real values and not none. If none, returns none. If valid input, then returns the dict.
    if title is None or genre is None or rating is None:
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
    # create a dict with "watched" as key and empty list as value
    watched_movies = {
        "watched": []
    }
    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in watched_movies dictionary
    if not user_data:
        return user_data
    else:
        watched_movies["watched"].append(movie)
    
    return watched_movies




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

