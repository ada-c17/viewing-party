
# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
        return new_movie
    return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for index, movie in enumerate(user_data["watchlist"]):
        if movie["title"] == title:
            user_data["watched"].append(movie)
            del user_data["watchlist"][index]
    return user_data

            
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_count = len(user_data["watched"])
    if watched_count == 0:
        return 0.0
    else:
        return sum(movie["rating"] for movie in user_data["watched"]) / watched_count


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        max_count = 0
        most_watched_genre = None
        genre_count_dict = {}
        for movie in user_data["watched"]:
            current_genre = movie["genre"]
            current_count  = genre_count_dict.get(current_genre, 0) + 1
            if current_count > max_count:
                max_count = current_count
                most_watched_genre = current_genre
        return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# A helper function to get all distinct movies from friends' "watched" lists
def get_friends_watched(user_data):
    friends_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)
    return friends_watched_movies


def get_unique_watched(user_data):
    user_watched_movies = user_data["watched"]
    friends_watched_movies = get_friends_watched(user_data)

    user_unique_watched_movies = []
    for movie in user_watched_movies:
        if movie not in friends_watched_movies:
            user_unique_watched_movies.append(movie)

    return user_unique_watched_movies


def get_friends_unique_watched(user_data):
    user_watched_movies = user_data["watched"]
    friends_watched_movies = get_friends_watched(user_data)  
    
    friends_unique_watched_movies = []
    for movie in friends_watched_movies:
        if movie not in user_watched_movies:
            friends_unique_watched_movies.append(movie)

    return friends_unique_watched_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    not_watched_movies = get_friends_unique_watched(user_data)

    recommended_movies = []
    for movie in not_watched_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies


#  -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    not_watched_movies = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    recommended_movies = []
    for movie in not_watched_movies:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)

    return recommended_movies    


def get_rec_from_favorites(user_data):
    friends_watched_movies = get_friends_watched(user_data)

    recommended_movies = []
    for movie in user_data["favorites"]:
        if movie not in friends_watched_movies:
            recommended_movies.append(movie)

    return recommended_movies