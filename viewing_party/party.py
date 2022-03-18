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
    print(user_data["watchlist"])
    # for user
    # if title in user_data["watchlist"]:
    #     user_data["watchlist"].remove(title)
    #     user_data["watched"].append(title)
    # return user_data

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
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

