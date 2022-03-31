# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None
    # new_movie["title"] = title
    # new_movie["genre"] = genre
    # new_movie["rating"] = rating
    # return new_movie
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie_dic in user_data["watchlist"]:
        if movie_dic["title"] == title:
            user_data["watchlist"].remove(movie_dic)
            user_data["watched"].append(movie_dic)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    total = 0
    for ele in user_data["watched"]:
        total += ele["rating"]
    return total/len(user_data["watched"])
# retun round( total/len(user_data["watched"]), 1)


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        # don't use  user_data["watched"]==[], since we need to check both user_data["watched"] and user_data are Falsey or not.
        # In the rare case that user_data or user_data["watched"] is passed in as None or an empty set, list, or tuple
        # then code won't throw an error trying to find a non-existing "watched" key.
        return None
    my_dic = {}
    max = 0
    result = ""
    for movie in user_data["watched"]:
        if movie["genre"] in my_dic:
            my_dic[movie["genre"]] += 1
        else:
            my_dic[movie["genre"]] = 1
    for movie_name, watched_time in my_dic.items():
        if watched_time > max:
            max = watched_time
            result = movie_name
    return result

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    mine = user_data["watched"]
    result = []
    if not mine:
        return result

    friends_movie = []
    for friend in user_data["friends"]:
        friends_movie += friend["watched"]
    for movie in mine:
        if not movie in friends_movie:
            result.append(movie)
    return result


def get_friends_unique_watched(user_data):
    mine = user_data["watched"]
    friends_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie:
                friends_movie.append(movie)
    result = []
    if not friends_movie:
        return result

    for movie in friends_movie:
        if movie not in mine:
            result.append(movie)
    return result


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    result = []
    friend_unique = get_friends_unique_watched(user_data)
    if not friend_unique or not user_data["subscriptions"]:
        return result
    for movie in friend_unique:
        if movie["host"] in user_data["subscriptions"]:
            result.append(movie)
    return result

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    result = []
    if not user_data["watched"]:
        return result
    most_genre = get_most_watched_genre(user_data)

    friend_unique = get_friends_unique_watched(user_data)
    if not friend_unique or not most_genre:
        return result
    for movie in friend_unique:
        if movie["genre"] == most_genre:
            result.append(movie)
    return result


def get_rec_from_favorites(user_data):
    result = []
    only_user_watched_movies = get_unique_watched(user_data)
    if not user_data["watched"] or not user_data["favorites"]:
        return result
    for movie in user_data["favorites"]:
        if movie in only_user_watched_movies:
            result.append(movie)
    return result
