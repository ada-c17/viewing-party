# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
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
            user_data["watched"].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if not user_data["watched"]:
        return 0.0
    else:
        return (sum(ratings) / len(ratings))

def get_most_watched_genre(user_data):
    most_watched = {}
    genres = []

    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    for genre in genres:
        if genre in most_watched:
            most_watched[genre] += 1
        else:
            most_watched[genre] = 1

    if user_data["watched"] == []:
        return None
    else:
        dict_values = list(most_watched.values())
        dict_key = list(most_watched.keys())

        most_watched_genre = dict_key[dict_values.index(max(dict_values))]

        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    final_list = [] # add in title dictionaries

    for watched in user_data["watched"]:
        if watched in final_list:
            final_list
        else:
            final_list.append(watched)

    for friend in user_data["friends"]:
        for title in friend["watched"]:
            if title in final_list:
                final_list.remove(title)
            else:
                final_list

    return final_list

# Return a list of dictionaries, that represents a list of movies
def get_friends_unique_watched(user_data):
    final_list = [] # add in title dictionaries

    for friend in user_data["friends"]:
        for title in friend["watched"]:
            if title in final_list:
                final_list
            else:
                final_list.append(title)

    for watched in user_data["watched"]:
        if watched in final_list:
            final_list.remove(watched)
        else:
            final_list

    return final_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_list = [] # a list of dictionaries that are movies
    friends_unique_movies = get_friends_unique_watched(user_data)

    for rec in friends_unique_movies:
        if rec["host"] in user_data["subscriptions"] and rec not in user_data["watched"]:
            recommended_list.append(rec)

    return recommended_list
    # Return a list of dictionaries, that represents a list of recommended movies

    # recommended_movies = [for movie in friends_unique_movies if (movie["host"] in user_data["subscriptions"] and movie not in user_data['watched'])]
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_rec = []
    users_most_watched_genre = get_most_watched_genre(user_data)
    friends_watched = user_data["friends"]
    print(user_data)

    for friend in friends_watched:
        for movie in friend["watched"]:
            if movie["genre"] == users_most_watched_genre and movie not in user_data["watched"] and movie not in genre_rec:
                genre_rec.append(movie)

    return genre_rec

def get_rec_from_favorites(user_data):
    users_movies = user_data["favorites"]
    recs = []
    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for fav in users_movies:
        if fav not in friends_watched:
            recs.append(fav)

    return recs