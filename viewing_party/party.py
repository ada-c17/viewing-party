# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    new_movie = {}
    keys = ["title", "genre", "rating"]
    values = [movie_title, genre, rating]

    if None in values:
        return None
    if len(keys) == len(values):
        new_movie = dict(zip(keys, values))
        return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        for category, item in movie.items():
            if category == "title" and item == title:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = []
    for dict in user_data["watched"]:
        ratings.append(dict["rating"])
    if ratings == []:
        return 0.0
    else:
        return sum(ratings) / len(ratings)


def get_most_watched_genre(user_data):
    genre_map = {}
    for dict in user_data["watched"]:
        if dict["genre"] not in genre_map:
            genre_map[(dict["genre"])] = 1
        else:
            genre_map[(dict["genre"])] += 1
    if genre_map == {}:
        return None
    else:
        return max(genre_map, key=genre_map.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # Create list of combined friend's movies
    friends_movies_list = [] 
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if movie not in friends_movies_list:
                friends_movies_list.append(movie)
    # Remove movies from user_data if not unique
    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_movies_list:
            unique_watched.append(movie)
    return unique_watched


def get_friends_unique_watched(user_data):
    # Create list of combined friend's movies
    friends_movies_list = [] 
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if movie not in friends_movies_list:
                friends_movies_list.append(movie)
    # Remove movies from friends_movies_list if not unique
    friends_unique_watched = []
    for movie in friends_movies_list:
        if movie not in user_data["watched"]:
            friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    if most_watched_genre is not None:
        for movie in friends_unique_watched:
            if movie["genre"] in most_watched_genre:
                recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []
    unique_watched = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in unique_watched:
            recommended_movies.append(movie)
    return recommended_movies