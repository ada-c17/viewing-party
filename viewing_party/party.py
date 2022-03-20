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
    average = 0
    watched_list_length = len(janes_data["watched"])
    if watched_list_length == 0:
        return average
    else:
        for movie in range(watched_list_length):
            total_rating += janes_data["watched"][movie]["rating"]
            average = total_rating / watched_list_length
    return average

def get_most_watched_genre(janes_data):
    if len(janes_data["watched"]) == 0:
        return None
    else:
        genre_counting_dict = {}
        for movie in range(len(janes_data["watched"])):
            if janes_data["watched"][movie]["genre"] not in genre_counting_dict:
                genre_counting_dict[janes_data["watched"][movie]["genre"]] = 1
            else:
                genre_counting_dict[janes_data["watched"][movie]["genre"]] += 1
    popular_genre = max(genre_counting_dict, key = genre_counting_dict.get)
    return popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------