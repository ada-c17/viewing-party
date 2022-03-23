# ------------- WAVE 1 --------------------

from audioop import avg
from sys import argv
import pprint
pp = pprint.PrettyPrinter(indent=4)

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

def get_watched_avg_rating(user_data):
    movies = user_data["watched"]
    summation = 0

    if len(movies) == 0:
        return 0.0
    
    for movie_dict in movies:
        summation += movie_dict["rating"] 

    return summation / len(movies)


def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    if watched_movies == []:
        return None
    logbook = {}
    
    for movie in watched_movies:
        genre = movie["genre"]


        if genre in logbook:
            logbook[genre] += 1
        else:
            logbook[genre] = 1
            
    max_count = 0
    most_watched_genre = ""

    for genre, count in logbook.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre
    
    pp.pprint(most_watched_genre)
    return most_watched_genre



        







# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

