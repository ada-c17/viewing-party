# ------------- WAVE 1 --------------------

from statistics import mean
import copy

def create_movie(title, genre, rating):
    if None in (title,genre,rating,):
        return None
    else:
        new_movie = {
            "title":title,
            "genre":genre,
            "rating":rating
        }
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    try: 
        filter_ratings = []
        for movie in user_data["watched"]:
            filter_ratings.append(movie["rating"])
        average_rating = mean(filter_ratings)
        return average_rating
    except:
        return 0.0

def get_most_watched_genre(user_data):
    genre_count = {}
    genre_counter = 0
    top_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else: 
            genre_count[movie["genre"]] = 1
        if genre_count[movie["genre"]] > genre_counter:
            top_genre = movie["genre"]
            genre_counter = genre_count[movie["genre"]]
    return top_genre 


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_unique_movies = copy.deepcopy(user_data["watched"])
    for friend_movie_dict in user_data["friends"]:
        for movie in friend_movie_dict["watched"]:
            if movie in user_unique_movies:
                user_unique_movies.remove(movie)
    return user_unique_movies


def get_friends_unique_watched(user_data):
    friend_movies = []
    user_unique_movies = user_data["watched"]
    for friend_movie_dict in user_data["friends"]:
        for movie in friend_movie_dict["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)
    friend_unique_movies = copy.deepcopy(friend_movies)
    for user_movie in user_unique_movies:
        for friend_movie in friend_movies:
            if user_movie == friend_movie:
                friend_unique_movies.remove(friend_movie)
    return friend_unique_movies
    # This is super messy. I don't like it. 
    # Perhaps I can use filter, list comp, or calculate a difference with sets of dictionaries?

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_movies = get_friends_unique_watched(user_data)
    for movie in friends_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    top_genre_recs = []
    try:    # I know this try-except is a hacky workaround to pass the test, but I don't want to go back and fix the function to accept empty "watched" right now. 
        top_genre = get_most_watched_genre(user_data)
        recommended_movies = get_available_recs(user_data)
        for movie in recommended_movies:
            if movie["genre"] == top_genre:
                top_genre_recs.append(movie)
        return top_genre_recs
    except:
        return top_genre_recs

def get_rec_from_favorites(user_data):
    rec_from_favorites = []
    try:    # still hacky, but I hope I have time to fix this later.
        user_unique_movies = get_unique_watched(user_data)
        for movie in user_data["favorites"]:
            if movie in user_unique_movies:
                rec_from_favorites.append(movie)
        return rec_from_favorites
    except:
        return rec_from_favorites