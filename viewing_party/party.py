# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title":title,
        "genre":genre,
        "rating":rating
    }
    if title == None or genre == None or rating == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    if user_data == None or movie == None:
        return None

    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    if user_data == None or movie == None:
        return None

    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    if user_data == None or title == None or not type(title)==str :
        return None
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for item in range(len(watchlist)):
        if title == watchlist[item]["title"]:
            watched.append(watchlist[item])
            watchlist.remove(watchlist[item])
        
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating():
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

