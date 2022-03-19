# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title == None:
        return None
    elif genre == None:
        return None
    elif rating == None:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie):
    movie_index = -1

    # find index of watched movie in watchlist list
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            movie_index = i

    # if movie is found to be in watchlist
    if movie_index >= 0:
        # remove element at that index from watchlist list and add to variable
        watched_movie = user_data["watchlist"].pop(movie_index)

        # add variable to watched list
        user_data["watched"].append(watched_movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # add up ratings
    sum = 0
    average = 0
    if len(user_data["watched"]) > 0:
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        # divide total by number of movies (length of list) to get average
        average = sum / len(user_data["watched"])

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

