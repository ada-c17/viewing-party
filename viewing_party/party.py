# ------------- WAVE 1 --------------------

from sys import argv


def create_movie(movie_title, genre, rating):
    dict = {}

    if movie_title == None or genre == None or rating == None:
        return None 
    else:
        dict["title"] = movie_title
        dict["genre"] = genre
        dict["rating"] = rating

    return dict 


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    for i in user_data["watchlist"]: 
        if i["title"] == title:
            user_data["watched"].append(i)
            user_data["watchlist"].remove(i)
    
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

