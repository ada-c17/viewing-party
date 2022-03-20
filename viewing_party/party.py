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
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    length = len(user_data["watched"])
    rating = 0.0

    if length == 0:
        return rating 

    for movie in user_data["watched"]:
        rating += movie["rating"]

    avg = rating / length
    return avg


def get_most_watched_genre(user_data):
    most_watched = None 

    if len(user_data["watched"]) == 0:
        return most_watched

    freq = {}
    for movie in user_data["watched"]:
        if not movie["genre"] in freq:
            freq[movie["genre"]] = 1
        else:
            freq[movie["genre"]] += 1
    
    most_watched = max(freq, key=freq.get)

    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    pass


def get_friends_unique_watched(user_data):
    pass


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    pass 


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass


def get_rec_from_favorites(user_data):
    pass 
