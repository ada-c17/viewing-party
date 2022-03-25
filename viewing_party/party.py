import statistics
from statistics import mode

# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(title, genre, rating):
    """Creates a movie dict."""
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    """Adds movie to a user's watched list."""
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """Adds a movie to a user's watchlist."""
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    """Moves a movie from a user's watch list to their watched list."""
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            movie_dict = user_data["watchlist"].pop(i)
            user_data["watched"].append(movie_dict)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """Gets the average rating of movies a user has watched."""
    ratings = [] 
    watched_list = user_data["watched"]
    
    for movie in watched_list:
        ratings.append(movie["rating"]) 

    ratings_sum = 0.0
    for rating in ratings:
        ratings_sum += rating

    try:
        avg_rating = ratings_sum / len(ratings)
    except ZeroDivisionError:
        return 0.0
    return avg_rating

def get_most_watched_genre(user_data):
    """Finds a user's most watched genre."""
    genres = [] 
    watched_list = user_data["watched"] 

    for movie in watched_list:
        genres.append(movie["genre"])

    if genres:
        return mode(genres)
    else:
        return None
    
    return mode(genres)

# -----------------------------------------   
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    """Finds movies watched by a user that their friends have not watched."""
    watched_list = user_data["watched"] 
    friends_watched_list = []
    unique_movies = [] 

    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched_list.append(movie) 

    for movie in watched_list:
        if movie not in friends_watched_list:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    """Finds movies that user's friends have watched that the user has not watched."""
    watched_list = user_data["watched"]
    friends_watched_list = []
    friends_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)

    for movie in friends_watched_list:
        if movie not in watched_list:
            friends_unique_movies.append(movie)
    return friends_unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """Finds recommendations from user's friends that are available on a streaming service user has access to."""
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommendations = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)
    return recommendations 

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """Find recommendations from user's friend list that are user's favorite genre"""
    recommendations = []
    
    # Handle empty watched list
    if not user_data["watched"]:
        return recommendations
    
    available_recs = get_available_recs(user_data)

    # Find user's favorite genre
    genres = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genres:
            genres[movie["genre"]] = 1
        else:
            genres[movie["genre"]] += 1

    favorite_genre = max(genres, key=genres.get)

    for movie in available_recs:
        if movie["genre"] == favorite_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    """Give friends recommendations from user's favorites"""
    recommendations = []
    friends_not_watched = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in friends_not_watched:
            recommendations.append(movie)
    return recommendations





