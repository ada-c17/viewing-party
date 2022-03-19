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

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) > 0:
        # make new list of just genres
        genre_list = []

        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        
        most_watched_count = 0
        most_watched_genre = ''
        # iterate through genre list, updating most_watched_genre as counts increase
        for genre in genre_list:
            genre_count = genre_list.count(genre)
            if genre_count > most_watched_count:
                most_watched_count = genre_count
                most_watched_genre = genre

        return most_watched_genre
    else:
        return None
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

