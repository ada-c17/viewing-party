# ------------- WAVE 1 --------------------


from logging.handlers import WatchedFileHandler
from tkinter import W


def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie = {
            "title": title, 
            "genre": genre,
            "rating": rating}
        return new_movie
    else:
        new_movie = None
        return new_movie

# am i supposed to make this or is the test making it?
# user_data = {
#         "watched": [
#             {
#                 "title": "Title A",
#                 "genre": "Horror",
#                 "rating": 3.5

#             }
            
#         ]
#     }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie) 
            user_data["watched"].append(movie)
            return user_data

    return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_ratings = 0
    num_of_movies = len(user_data["watched"])
    
    if len(user_data["watched"]) < 1:
        watched_avg_rating = 0.0 
        return watched_avg_rating

    for movie in user_data["watched"]:
        total_ratings += movie["rating"]

    watched_avg_rating = total_ratings / num_of_movies

    return watched_avg_rating

def get_most_watched_genre(user_data):
    
    if len(user_data["watched"]) < 1:
        most_watched_genre = None 
        return most_watched_genre

    genre_count_dict = {}

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count_dict:
            genre_count_dict[movie["genre"]] = 1
        else: 
            genre_count_dict[movie["genre"]] += 1

    highest_count_sofar = 0
    highest_genre = None

    for genre, count in genre_count_dict.items():
        if count > highest_count_sofar:
            highest_count_sofar = count
            highest_genre = genre

    return highest_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.append(movie["title"])
    
    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    user_unique_watched_set = user_watched_set.difference(friend_watched_set)
    user_unique_watched_list = []

    for unique_movie in user_unique_watched_set:
        for movie in user_data["watched"]:
            if movie["title"] == unique_movie:
                user_unique_watched_list.append(movie)

    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.append(movie["title"])
    
    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    friend_unique_watched_set = friend_watched_set.difference(user_watched_set)
    friend_unique_watched_list = []

    for unique_movie in friend_unique_watched_set:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie not in friend_unique_watched_list:
                    if movie["title"] == unique_movie:
                        friend_unique_watched_list.append(movie)

    return friend_unique_watched_list




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    friends_unique_watched_list = get_friends_unique_watched(user_data)

    available_recommended_movies_list = []

    for movie in friends_unique_watched_list:
        for subscription in user_data["subscriptions"]:
            if subscription == movie["host"]:
                available_recommended_movies_list.append(movie)

    return available_recommended_movies_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_watched = get_friends_unique_watched(user_data)
    recommended_movies = []

    for movie in friend_unique_watched:
        if movie not in recommended_movies and movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):

    user_unique = get_unique_watched(user_data)
    rec_from_fav = []

    for favorite_movie in user_data["favorites"]:
        for unique_movie in user_unique:
            if favorite_movie["title"] == unique_movie["title"]:
                if favorite_movie not in rec_from_fav:
                    rec_from_fav.append(favorite_movie)
    return rec_from_fav

#HAZZAH