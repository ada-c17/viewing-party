# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        movies = None
    else:
        movies = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for watched_movie in user_data["watchlist"]:
        if watched_movie["title"] == title:
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

