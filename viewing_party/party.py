from statistics import mode

# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
        
    movie_dict = {
        "title" : title,
        "genre" : genre,
        "rating" : rating
    }

    return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie):

    for watchlist_movie in user_data["watchlist"]:
        if watchlist_movie["title"] == movie:
            user_data["watched"].append(watchlist_movie)
            user_data["watchlist"].remove(watchlist_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_of_ratings = 0
    average_rating = 0

    for movie in user_data["watched"]:
        total_of_ratings += movie["rating"] 
        average_rating = total_of_ratings / len(user_data["watched"])
        
    return average_rating


def get_most_watched_genre(user_data):
    all_watched_genres = []
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        all_watched_genres.append(movie["genre"])
    return mode(all_watched_genres)



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched_movies = []
    unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)
    for movie in user_data["watched"]:
        if movie not in friends_watched_movies:
            unique_movies.append(movie)
    return unique_movies


def get_friends_unique_watched(user_data):

    friends_unique_movies = []

    for friend in user_data["friends"]:
        if friend["watched"]:
            for movie in friend["watched"]:
                if movie not in user_data["watched"] and movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)

    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_recs = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    if "subscriptions" not in user_data:
        return []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            friends_recs.append(movie)
    return friends_recs



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    all_watched_genres = []
    friends_rec_by_genre = []

    # for friend in user_data["friends"]:
    #     if not friend["watched"]:
    #         watched = False
    #     else: 
    #         watched = True

    if user_data["watched"]:
        friends_recs = get_available_recs(user_data)
        for movie in user_data["watched"]:
            all_watched_genres.append(movie["genre"])
        for movie in friends_recs:
            if movie["genre"] in all_watched_genres:
                friends_rec_by_genre.append(movie)

    return friends_rec_by_genre


def get_rec_from_favorites(user_data):
    fav_recs = []
    unique_movies = get_unique_watched(user_data)
    for movie in unique_movies:
        if movie in user_data["favorites"]:
            fav_recs.append(movie)
    return fav_recs


