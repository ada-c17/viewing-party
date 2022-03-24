# ------------- WAVE 1 --------------------

from turtle import title
import copy

def create_movie(movie_title, genre, rating):
    new_movie = {"title" : movie_title , "genre" : genre , "rating" : rating }
    if movie_title == None or genre == None or rating == None:
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

def get_unique_watched(user_data):
    unique_movie_list = copy.deepcopy(user_data["watched"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in unique_movie_list:
                unique_movie_list.remove(movie)
    return unique_movie_list
        

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_list:
                friends_unique_list.append(movie)
    return friends_unique_list

def get_available_recs(user_data):
    recomended_list = []
    seen_by_friends = get_friends_unique_watched(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            try:
                if movie["host"] in user_data["subscriptions"] and movie in seen_by_friends:
                    recomended_list.append(movie)
            except KeyError:
                return recomended_list
    return recomended_list

def get_new_rec_by_genre(user_data):
    recomended_movies = []
    users_fav_genre = get_most_watched_genre(user_data)
    for movie in get_available_recs(user_data):
        if movie["genre"] == users_fav_genre:
            recomended_movies.append(movie)
    return recomended_movies


def get_rec_from_favorites(user_data):
    recs_from_favorites = []
    for movie in user_data["favorites"]:
        if movie in get_unique_watched(user_data):
            recs_from_favorites.append(movie)
    return recs_from_favorites


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

