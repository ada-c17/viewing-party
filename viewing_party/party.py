# ------------- WAVE 1 --------------------

from turtle import title


def create_movie(movie_title, genre, rating):
    new_movie = {"title" : movie_title , "genre" : genre , "rating" : rating }
    if movie_title == None:
        new_movie = None
        return new_movie
    elif genre == None:
        new_movie = None
        return new_movie
    elif rating == None:
        new_movie = None
        return new_movie
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] += [movie]
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    total = 0
    for movie in user_data["watched"]:
        total += movie["rating"]
    if len(user_data["watched"]) <= 0:
        average = 0.0
        return average
    elif len(user_data["watched"]) > 0:
        average = total / len(user_data["watched"])
        return average


def get_most_watched_genre(user_data):
    popular_genre = {}
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in popular_genre:
            popular_genre[movie["genre"]] = 1
        else:
            popular_genre[movie["genre"]] += 1
    best_genre = max(popular_genre, key = popular_genre.get)
    return best_genre




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

