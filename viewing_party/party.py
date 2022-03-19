# ------------- WAVE 1 --------------------

from re import T


def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][index]["title"]:
            watched_movie = user_data["watchlist"][index]
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0
    if len(user_data["watched"]) > 0:
        for movie_watched in user_data["watched"]:
            average_rating += movie_watched["rating"]
        return average_rating / len(user_data["watched"])
    else:
        return len(user_data["watched"])


def get_most_watched_genre(user_data):
    dict_genre_count = {}
    if len(user_data["watched"]) != 0:
        for movie_watched in user_data["watched"]:
            if movie_watched["genre"] not in dict_genre_count.keys():
                dict_genre_count[movie_watched["genre"]] = 1
            else:
                dict_genre_count[movie_watched["genre"]] += 1
        
        most_frequent_genre = max(dict_genre_count.values())
        for key,value in dict_genre_count.items():
            if value == most_frequent_genre:
                return key
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movie_list = []
    for index in range(len(user_data["friends"])):
        friends_movie_list += user_data["friends"][index]["watched"]
    
    user_unique_watched_list = []
    for unique_movie in user_data["watched"]:
        if unique_movie not in friends_movie_list:
            user_unique_watched_list.append(unique_movie)
    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    friends_movie_list_with_duplicate = []
    for index in range(len(user_data["friends"])):
        friends_movie_list_with_duplicate += user_data["friends"][index]["watched"]
    friends_movie_list_without_duplicate = []
    for movie in friends_movie_list_with_duplicate:
        if movie not in friends_movie_list_without_duplicate:
            friends_movie_list_without_duplicate.append(movie)

    friends_unique_watched_list = []
    for unique_movie in friends_movie_list_without_duplicate:
        if unique_movie not in user_data["watched"]:
            friends_unique_watched_list.append(unique_movie)
    return friends_unique_watched_list



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

