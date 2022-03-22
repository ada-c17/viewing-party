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
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        for movie_watched in user_data["watched"]:
            average_rating += movie_watched["rating"]
        return average_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):
    dict_genre_count = {}
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie_watched in user_data["watched"]:
            if movie_watched["genre"] not in dict_genre_count.keys():
                dict_genre_count[movie_watched["genre"]] = 1
            else:
                dict_genre_count[movie_watched["genre"]] += 1
    # example of dict_genre_count: {'Fantasy': 3, 'Action': 1, 'Intrigue': 2}
        for genre, count in dict_genre_count.items():
            if count == max(dict_genre_count.values()):
                return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movie_list_without_duplicate = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list_without_duplicate:
                friends_movie_list_without_duplicate.append(movie)
    user_unique_watched_list = []
    for unique_movie in user_data["watched"]:
        if unique_movie not in friends_movie_list_without_duplicate:
            user_unique_watched_list.append(unique_movie)
    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    friends_movie_list_without_duplicate = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
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
def get_available_recs(user_data):
    recommend_movies = []
    movies_at_least_friends_watched = get_friends_unique_watched(user_data)
    for movie in range(len(movies_at_least_friends_watched)):
        if movies_at_least_friends_watched[movie]["host"] in user_data["subscriptions"]:
            recommend_movies.append(movies_at_least_friends_watched[movie])
    return recommend_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    get_new_rec_list_by_genre = []
    movies_at_least_friends_watched = get_friends_unique_watched(user_data)
    for movie in range(len(movies_at_least_friends_watched)):
        if movies_at_least_friends_watched[movie]["genre"] == get_most_watched_genre(user_data):
            get_new_rec_list_by_genre.append(movies_at_least_friends_watched[movie])
    return get_new_rec_list_by_genre

def get_rec_from_favorites(user_data):
    friends_movie_list_without_duplicate = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list_without_duplicate:
                friends_movie_list_without_duplicate.append(movie)
    rec_to_friends_from_favorites = []
    for movie in range(len(user_data["favorites"])):
        if user_data["favorites"][movie] not in friends_movie_list_without_duplicate:
            rec_to_friends_from_favorites.append(user_data["favorites"][movie])
    return rec_to_friends_from_favorites

