# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    movie = {}
    movie_set = {title, genre, rating}

    if None in movie_set:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    
    return movie

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if title != movie["title"]:
            continue
        else:
            movie_index = user_data["watchlist"].index(movie)
            removed_movie = user_data["watchlist"].pop(movie_index)
            add_to_watched(user_data, removed_movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    total = 0

    if not user_data["watched"]:
        return 0.0
    
    for movie in user_data["watched"]:
        total += movie["rating"]
    
    average = total / len(user_data["watched"])

    return average

def get_most_watched_genre(user_data):
    
    compare_dict = {}

    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in compare_dict:
            compare_dict[genre] = 0
        compare_dict[genre] += 1
    
    most_watched_genre = max(compare_dict, key=compare_dict.get)

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    friends_movie_list = []

    for friend in user_data["friends"]:
        friends_movie_list.extend(friend["watched"])
    
    unique_movies = []

    for movie in user_data["watched"]:
        if movie not in friends_movie_list:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):

    friends_movie_list = []

    for friend in user_data["friends"]:
        friends_movie_list.extend(friend["watched"])
    
    unique_movies = []

    for movie in friends_movie_list:
        if movie not in user_data["watched"] and movie not in unique_movies:
            unique_movies.append(movie)

    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    unique_movies = get_friends_unique_watched(user_data)
    friends_rec = []

    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            friends_rec.append(movie)

    return friends_rec

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    if "favorites" not in user_data:
        return []

    fav_genre_set = set()

    for fav_movie in user_data["favorites"]:
        fav_genre_set.add(fav_movie["genre"])
    
    friends_rec = get_available_recs(user_data)

    recommendations = []

    for movie in friends_rec:
        if movie["genre"] in fav_genre_set:
            recommendations.append(movie)


    return recommendations

def get_rec_from_favorites(user_data):

    if "favorites" not in user_data:
        return []

    friends_movie_list = []

    for friend in user_data["friends"]:
        friends_movie_list.extend(friend["watched"])

    recommendations = []

    for movie in user_data["favorites"]:
        if movie not in friends_movie_list and movie not in recommendations:
            recommendations.append(movie)

    return recommendations