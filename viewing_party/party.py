# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None
    return {"title":title, "genre":genre,"rating":rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, watched_movie_title):
    updated_watchlist = []
    for movie in user_data["watchlist"]:
        if movie["title"] == watched_movie_title:
            user_data["watched"].append(movie)
        else:
            updated_watchlist.append(movie)
    user_data["watchlist"] = updated_watchlist
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    rating_sum = 0
    for movie in user_data["watched"]:
        rating_sum += movie["rating"]
    return rating_sum / len(user_data["watched"])

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    watched_genre_frequencies = {}
    for movie in user_data["watched"]:
        if movie["genre"] in watched_genre_frequencies.keys():
            watched_genre_frequencies[movie["genre"]] += 1
        else:
            watched_genre_frequencies[movie["genre"]] = 1
    
    current_top = ["",0]
    for genre, count in watched_genre_frequencies.items():
        if count > current_top[1]:
            current_top = [genre, count]
    return current_top[0]

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# TODO: consider refactoring these using set comparisons

def get_unique_watched(user_data):
    common_titles_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in user_data["watched"]:
                common_titles_set.add(movie["title"])
    
    uniquely_watched = []
    for movie in user_data["watched"]:
        if movie["title"] not in common_titles_set:
            uniquely_watched.append(movie)
    return uniquely_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie not in user_data["watched"] and
                    movie not in friends_unique_watched):
                friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_recs = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie not in user_data["watched"] and
                    movie["genre"] == genre and
                    movie not in recs):
                recs.append(movie)
    return recs

def get_rec_from_favorites(user_data):
    if "favorites" not in user_data.keys():
        return []

    recs = list(user_data["favorites"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in recs:
                recs.remove(movie)
    return recs
