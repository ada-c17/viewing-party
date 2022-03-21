# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
        return None
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

def watch_movie(user_data, title):
    index = 0
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            move_movie = movie
            break
        index += 1
    if index > len(user_data["watchlist"]):
        return user_data
    try:
        user_data["watched"].append(move_movie)
        user_data["watchlist"].pop(index)
    except(UnboundLocalError):
        pass
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total = 0
    num_iterations = 0
    for i in user_data["watched"]:
        num_iterations += 1
        total += i['rating']
    try:
        average = total / num_iterations
    except(ZeroDivisionError):
        return 0.0
    return average
    
def get_most_watched_genre(user_data):
    if user_data["watched"] == []:
        return None
    genre_tally = {}
    for movie in user_data["watched"]:
        try:
            genre_tally[movie["genre"]] += 1
        except (KeyError):
            genre_tally[movie["genre"]] = 1
    most_watched = (None, 0)
    for item in genre_tally.items():
        if item[1] > most_watched[1]:
            most_watched = (item[0], item[1])
    return most_watched[0]




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

