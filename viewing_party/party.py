# ------------- WAVE 1 --------------------

from re import U


def create_movie(title, genre, rating):
    if title != None and genre != None and rating != None:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    else:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data = add_to_watched(user_data, movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    lst = []
    sum = 0
    for item in user_data["watched"]:
        lst.append(item["rating"])
    for number in lst:
        sum += number
    if lst:
        return sum / len(lst)
    else:
        return 0.0

def get_most_watched_genre(user_data):

    most_watched = {}
    for movie in user_data["watched"]:
        most_watched.setdefault(movie["genre"], 0)
        most_watched[movie["genre"]] += 1

    max_value = 0
    max_key = None

    for key, value in most_watched.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    list_watched = []
    for movie in user_data["watched"]:
        list_watched.append(movie)

    friends_watched_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])

    list_unique = []
    for movie in list_watched:
        if movie["title"] not in friends_watched_set:
            list_unique.append(movie)
    return list_unique

def get_friends_unique_watched(user_data):
    set_watched = set()
    for movie in user_data["watched"]:
        set_watched.add(movie["title"])

    friends_watched_dict = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_dict[movie["title"]] = movie

    list_unique = []
    for key, value in friends_watched_dict.items():
        if key not in set_watched:
            list_unique.append(value)

    return list_unique
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    set_watched = set()
    for movie in user_data["watched"]:
        set_watched.add(movie["title"])

    friends_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    list_friends_watched = []
    for movie in friends_watched_list:
        if movie["title"] not in set_watched:
            list_friends_watched.append(movie)

    recs_list = []
    for movie in list_friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            recs_list.append(movie)

    return recs_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)

    set_watched = set()
    for movie in user_data["watched"]:
        set_watched.add(movie["title"])

    friends_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    list_friends_watched = []
    for movie in friends_watched_list:
        if movie["title"] not in set_watched:
            list_friends_watched.append(movie)

    rec_by_genre_list = []
    for movie in list_friends_watched:
        if movie["genre"] == most_watched_genre:
            rec_by_genre_list.append(movie)
    return rec_by_genre_list

