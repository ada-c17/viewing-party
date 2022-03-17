# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    
    movie = {}
    movie['title'] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    watched_movie = {}
    #find movie_title in user_data["watchlist"]
    for movie in user_data["watchlist"]:
        # movie is a dict
        if movie['title'] == movie_title:
            # add movieto user_data["watched"]
            user_data["watched"].append(movie)
            # remove movie_title in user_data["watchlist"]
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

