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




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

