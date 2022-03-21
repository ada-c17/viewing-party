# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

from logging.handlers import WatchedFileHandler


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

def watch_movie(user_data, movie_to_watch):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie_to_watch:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0
    average = 0
    watched_list_length = len(user_data["watched"])
    if watched_list_length == 0:
        return average
    else:
        for movie in range(watched_list_length):
            total_rating += user_data["watched"][movie]["rating"]
            average = total_rating / watched_list_length
    return average

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_counting_dict = {}
        for movie in range(len(user_data["watched"])):
            if user_data["watched"][movie]["genre"] not in genre_counting_dict:
                genre_counting_dict[user_data["watched"][movie]["genre"]] = 1
            else:
                genre_counting_dict[user_data["watched"][movie]["genre"]] += 1
    popular_genre = max(genre_counting_dict, key = genre_counting_dict.get)
    return popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movies = []
    for friend_movie_dict_index in range(len(user_data["friends"])):
        friends_movies += user_data["friends"][friend_movie_dict_index]["watched"]

    users_unique_movies = []
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            users_unique_movies.append(movie)

    return users_unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = []
    for friend_movie_dict_index in range(len(user_data["friends"])):
        friends_movies += user_data["friends"][friend_movie_dict_index]["watched"]

    friends_unique_watched = []
    for movie in friends_movies:
        if movie not in user_data["watched"]:
            friends_unique_watched.append(movie)
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------