# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title": title, 
        "genre": genre,
        "rating": rating 
    }

    if title == None or genre == None or rating == None:
        new_movie = None 
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    if title in user_data["watchlist"]:
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
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

