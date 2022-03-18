import copy

# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    updated_data = copy.deepcopy(user_data)

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            updated_data["watched"].append(movie)
            updated_data["watchlist"].remove(movie)

    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    total_points = 0.0
    total_movies = 0
    avg_rating = 0.0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            total_movies += 1
            total_points += movie["rating"]
        avg_rating = total_points/total_movies
    return avg_rating


def get_most_watched_genre(user_data):
    most_watched_genre = None
    genre_count_dict = {}
    if user_data["watched"]:
        for movie in user_data["watched"]:
            if movie["genre"] in genre_count_dict:
                genre_count_dict[movie["genre"]] += 1
            else:
                genre_count_dict[movie["genre"]] = 1
        counts_list = list(genre_count_dict.values())
        for genre, count in genre_count_dict.items():
            if count == max(counts_list):
                most_watched_genre = genre

    return most_watched_genre

# ******** note to self: maybe update to handle a tie in most watched genres ********

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    unique_watched = []
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched

    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------


def get_available_recs(user_data):
    recommended = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recommended.append(movie)

    return recommended

    # -----------------------------------------
    # ------------- WAVE 5 --------------------
    # -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommended = []

    genre = get_most_watched_genre(user_data)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == genre:
                recommended.append(movie)

    return recommended


def get_rec_from_favorites(user_data):
    recommended = []
    friends_watched = []
    if "favorites" in user_data.keys():
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                friends_watched.append(movie)

        for movie in user_data["favorites"]:
            if movie not in friends_watched:
                recommended.append(movie)

    return recommended
