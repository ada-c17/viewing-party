# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    new_movie = {"title" : title, "genre" : genre, "rating" : rating}
    if new_movie["title"] == None or new_movie["genre"] == None or new_movie["rating"] == None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {
        "watched": [movie]
    }
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data

def watch_movie(janes_data, movie_to_watch):
    for i in range(len(janes_data["watchlist"])):
        if janes_data["watchlist"][i]["title"] == movie_to_watch:
            janes_data["watched"].append(janes_data["watchlist"][i])
            janes_data["watchlist"].pop(i)
    return janes_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(janes_data):
    total_rating = 0
    for movie in range(len(janes_data["watched"])):
        total_rating += janes_data["watched"][movie]["rating"]
        average = total_rating / len(janes_data["watched"])
    return average


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------