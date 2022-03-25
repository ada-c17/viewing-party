
# --------- UTILITY FUNCTIONS -------------

def make_list_unique(list_of_dicts):
    #returns a list that has no duplicate dicts
    unique_list = []
    for dct in list_of_dicts:
        if dct not in unique_list:
            unique_list.append(dct)
    return unique_list

def get_friends_watched_movies(user_data):
    friends_watched_movies = []
    for dct in user_data["friends"]:
        for movie in dct["watched"]:
            friends_watched_movies.append(movie)
    return friends_watched_movies


# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    if (title is None) or (genre is None) or (rating is None):
        return None
    return {"title":title, "genre":genre, "rating":rating,}


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    '''
    Cycles through watchlist, finds matching entry, then pops that
    entry off of watchlist and appends it to watched.
    '''
    for i, movie in enumerate(user_data["watchlist"]):
        if movie["title"] == movie_title:
            user_data["watched"].append(user_data["watchlist"].pop(i))
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_list = [movie["rating"] for movie in user_data["watched"]]
    if len(ratings_list) == 0:
        return 0
    else:
        return sum(ratings_list) / len(ratings_list)


def get_most_watched_genre(user_data):
    genre_list = [movie["genre"] for movie in user_data["watched"]]
    if len(genre_list) == 0:
        return None
    else:
        genre_count_dict = {genre:0 for genre in genre_list}

        for genre in genre_list:
            if genre in genre_count_dict.keys():
                genre_count_dict[genre] += 1

        max_count = 0
        max_count_genre = None
        for genre, count in genre_count_dict.items():
            if count > max_count:
                max_count = count
                max_count_genre = genre

        return max_count_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched_movies = get_friends_watched_movies(user_data)
    return [movie for movie in user_data["watched"] if movie not in friends_watched_movies]


def get_friends_unique_watched(user_data):
    friends_watched_movies = get_friends_watched_movies(user_data)
    return make_list_unique([movie for movie in friends_watched_movies if movie not in user_data["watched"]])


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''
    return list of movies that:
    1. the user has not watched
    2. the user's friend has watched
    3. is compatible with their subscriptions
    '''
    friends_watched_movies = [movie for movie in get_friends_watched_movies(user_data) if movie["host"] in user_data["subscriptions"]]
    return make_list_unique([movie for movie in friends_watched_movies if movie not in user_data["watched"]])


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    fave_genre = get_most_watched_genre(user_data)
    friends_unique_watched_movies = get_friends_unique_watched(user_data)

    return [movie for movie in friends_unique_watched_movies if movie["genre"] == fave_genre]


def get_rec_from_favorites(user_data):
    friends_watched_movies = get_friends_watched_movies(user_data)
    return [movie for movie in user_data["favorites"] if movie not in friends_watched_movies]
