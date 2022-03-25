# ------------- WAVE 1 --------------------

from typing import Counter


def create_movie(title, genre, rating):
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    
    ratings = [movie["rating"] for movie in user_data["watched"]]
    Sum = sum(ratings)
    Count = len(ratings)

    if len(user_data["watched"]) == 0:
        return 0.0
    return Sum/Count
    
def get_most_watched_genre(user_data):
    most_watched = ""
    max_value = 0
    genres = [movie["genre"] for movie in user_data["watched"]]
    genres_dict = Counter(genres)

    if len(user_data["watched"]) == 0:
        return None
    for key, value in genres_dict.items():
        if value >= max_value:
            max_value = value
            most_watched = key
    return most_watched
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = []
    friends_titles = []
    for friend in user_data["friends"]:
        for i in range(len(friend["watched"])):
            friends_titles.append(friend["watched"][i]["title"])
            
    friends_titles_set= set(friends_titles)

    for movie in user_data["watched"]:
        if not movie["title"] in friends_titles_set:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = []
    friends_unique_watched = []
    for friend in user_data["friends"]:
            friends_movies.extend(friend["watched"])
    
    for movie in friends_movies:
        if len(user_data["watched"]) == 0: 
            break
        elif not movie in user_data["watched"] and not movie in friends_unique_watched:
            friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    i = 0
    while i < len(friends_unique_watched):
        if friends_unique_watched[i]["host"] in user_data["subscriptions"]:
            recommended_movies.append(friends_unique_watched[i])
        i = i + 1
    return recommended_movies
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_list = []
    most_watched_genre = get_most_watched_genre(user_data)
    recom_movies = get_available_recs(user_data)
    
    i = 0
    while i < len(recom_movies):
        if recom_movies[i]["genre"] == most_watched_genre:
            recommended_list.append(recom_movies[i])
        i = i + 1
    return recommended_list
    
def get_rec_from_favorites(user_data):

    user_favorites = [movie for movie in user_data["favorites"]]
    user_unique_movies = get_unique_watched(user_data)

    recommended_movie = [movie for movie in user_favorites if movie in user_unique_movies]
    return recommended_movie
