# ------------- WAVE 1 --------------------

from tokenize import generate_tokens


def create_movie(title, genre, rating):

    if title == None or genre == None or rating == None:
        return None

    new_movie = {"title": title, "genre": genre, "rating": rating}

    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watchlist"].remove(item)
            user_data["watched"].append(item)
    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    ratings = 0

    if user_data["watched"] == []:
        return 0

    for watched in user_data["watched"]:
        ratings += watched["rating"]
    average = ratings / len(user_data["watched"])
    
    return average

def get_most_watched_genre(user_data):
    genre_dict= {}

    if user_data["watched"] == []:
        return None

    for watched in user_data["watched"]:
        if watched["genre"] in genre_dict:
            genre_dict[watched["genre"]] += 1
        else:
            genre_dict[watched["genre"]] = 1

    max_genre = max(genre_dict, key = genre_dict.get)

    return max_genre

# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    unique_list = []
    for movie in get_my_unique_watched(user_data):
        if movie not in get_friends_watched(user_data):
            unique_list.append(movie)
    return unique_list

def get_my_unique_watched(user_data):
    return user_data["watched"]

def get_friends_watched(user_data):
    movie_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movie_list.append(movie)
    return movie_list

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    for movie in get_friends_watched(user_data):
        if movie not in get_my_unique_watched(user_data) and \
            movie not in friends_unique_list: 
                friends_unique_list.append(movie)
        
    return friends_unique_list


# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    user_recs = []
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            user_recs.append(movie)
    return user_recs


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    genre_recs = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            genre_recs.append(movie)
    return genre_recs

def get_rec_from_favorites(user_data):
    fav_rec_list = []
    for movie in user_data["favorites"]:
        if movie not in get_friends_watched(user_data):
            fav_rec_list.append(movie)

    return fav_rec_list



