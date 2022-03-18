from multiprocessing.connection import wait
from typing import Optional
# ------------- WAVE 1 --------------------

def create_movie(title: str, genre: str, rating: float) -> Optional[dict]:
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
        return new_movie
    return None

# comment
def add_to_watched(user_data: dict, movie: dict) -> dict:
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data: dict, movie: dict) -> dict:
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data: dict, title: str) -> dict:
    # get movie data from watchlist
    for index, movie in enumerate(user_data["watchlist"]):
        if movie["title"] == title:
            user_data["watched"].append(movie)
            del user_data["watchlist"][index]
    return user_data

            
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data: dict) -> float:
    watched_count = len(user_data["watched"])
    if watched_count == 0:
        return 0.0
    else:
        return sum(movie["rating"] for movie in user_data["watched"]) / watched_count

    

def get_most_watched_genre(user_data: dict) -> Optional[str]:
    if len(user_data["watched"]) == 0:
        return None
    else:
        max_count = 0
        most_watched_genre = None
        genres = {}
        for movie in user_data["watched"]:
            current_genre = movie["genre"]
            current_count  = genres.get(current_genre, 0) + 1
            if current_count > max_count:
                max_count = current_count
                most_watched_genre = current_genre
        return most_watched_genre

# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data: dict) -> list[dict]:
    user_watched_movies = user_data["watched"]

    # Get all unique titles from friends' watched lists:
    friends_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)
   
    user_unique_movies = []
    for movie in user_watched_movies:
        if movie not in friends_watched_movies:
            user_unique_movies.append(movie)
    return user_unique_movies
    



def get_friends_unique_watched(user_data: dict) -> list[dict]:
    # Get all unique movies from friends' watched lists:
    friends_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)
   

    user_watched_movies = user_data["watched"]
    friends_unique_watched_movies = []
    for movie in friends_watched_movies:
        if movie not in user_watched_movies:
            friends_unique_watched_movies.append(movie)
    return friends_unique_watched_movies 
   
user_data = {
    'watched': [
        {"title": 'D', "rating": 3.0},
        {"title": 'B', "rating": 3.1},
    ],
    'friends': [
        {'watched': [{"title": 'A', "rating": 3.0}, {"title": 'B', "rating": 3.1}]},
        {'watched': [{"title": 'A', "rating": 3.4}, {"title": 'C', "rating": 4.0}]},
        {'watched': [{"title": 'A', "rating": 3.4}, {"title": 'B', "rating": 4.0}]},
    ]
}
print(get_friends_unique_watched(user_data))
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

