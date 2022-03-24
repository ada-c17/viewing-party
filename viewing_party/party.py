# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        movies = None
    else:
        movies = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for watched_movie in user_data["watchlist"]:
        if watched_movie["title"] == title:
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    rating_count = 0
    for movie in user_data["watched"]:
        rating_count += 1
        avg_rating += movie["rating"]
    if rating_count > 0:
        return avg_rating / rating_count
    else:
        return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_count = {}
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_count:
                genre_count[movie["genre"]] = 1
            else:
                genre_count[movie["genre"]] += 1
            return max(genre_count, key=genre_count.get)

# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    user_unique_movies = []
    for user_movie in user_data["watched"]:
        movie_is_unique = True
        for friend in user_data["friends"]:
            if user_movie in friend["watched"]:
                    movie_is_unique = False
        if movie_is_unique:
            user_unique_movies.append(user_movie)
    return user_unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_data["watched"] \
            and friend_movie not in friends_unique_movies:
                friends_unique_movies.append(friend_movie)
    return friends_unique_movies

# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    available_recs = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    return available_recs

# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    recs = []
    fav_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["genre"] == fav_genre and movie not in recs:
            recs.append(movie)
    return recs

def get_rec_from_favorites(user_data):
    recs = []
    user_unique_movies = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in user_unique_movies:
            recs.append(movie)
    return recs
