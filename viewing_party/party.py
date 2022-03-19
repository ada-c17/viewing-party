

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # creating a dictionary that stores the variables passed into the function as the values
    new_movie_added = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # checks to make sure that the variables passed into the function are real values and not none. If none, returns none. If valid input, then returns the dict.
    if title is None or genre is None or rating is None:
        return None
    else:
        return new_movie_added

def add_to_watched(user_data, movie):
    watched_movies = user_data
    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in watched_movies dictionary
    if not watched_movies:
        return watched_movies
    else:
        watched_movies["watched"].append(movie)
    
    return watched_movies

def add_to_watchlist(user_data, movie):
    movies_to_watch = user_data

    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in movies_to_watch dictionary
    if not movies_to_watch:
        return movies_to_watch
    else:
        movies_to_watch["watchlist"].append(movie)
    
    return movies_to_watch

def watch_movie(user_data, title):
    all_movies = user_data
    
    for i in range(len(user_data["watchlist"])):
        if title == all_movies["watchlist"][i]["title"]:
            all_movies["watchlist"].remove(all_movies["watchlist"][i])
            all_movies["watched"].append(title)

    return all_movies


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

