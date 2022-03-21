# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {
        "title": title, 
        "genre": genre,
        "rating": rating
    }

    if None in movie.values():
        return None
    else:
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in list(user_data["watchlist"]):
        if movie["title"] == movie_title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    if not user_data["watched"]:
        return 0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    genre_count = {}
    genre_list = []
# I guess this works.. has functionality to deal with
# any list of genres instead of hardcoding counters for each.
# Maybe better with a helper function called get_genre_list()?
    for movie in user_data['watched']:
        count = 0
# Add to running list of genres
        genre_list.append(movie["genre"])
# Iterate over the list to update a counter
        for genre in genre_list:
            if genre == movie["genre"]:
                count += 1
# Add a key with the genre name and value with count to a dict
        genre_count[movie["genre"]] = count
# Iterate over the dict and return the genre with highest count
    for genre in genre_count:
        if genre_count[genre] == max(genre_count.values()):
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    users_unique_watched = list(user_data["watched"])
    for movie in user_data["watched"]:
        for friend in range(len(user_data["friends"])):
            if movie in user_data["friends"][friend]["watched"] and movie in users_unique_watched:
                users_unique_watched.remove(movie)
                
    return users_unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in range(len(user_data["friends"])):
        for movie in user_data["friends"][friend]["watched"]:
            if movie not in friends_unique_watched and movie not in user_data["watched"]:
                friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    reccomendations = []
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            reccomendations.append(movie)
    return reccomendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    recommendations = []

    for movie in friends_movies:
        if movie["genre"] is favorite_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    unique_movies = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in unique_movies:
            recommendations.append(movie)
    return recommendations

