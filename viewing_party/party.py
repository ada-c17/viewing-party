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

def get_unique_watched(user_data):
    difference_movies = []
    watched_movies = user_data["watched"]
    friends = user_data["friends"]

    for movie in watched_movies:
        found = False 
        
        for friend in friends:
            friend_movies = friend["watched"] 
            for friend in friend_movies:
                if movie["title"] == friend["title"]:
                    found = True 
                    break 
                
        if found == False:
            difference_movies.append(movie)    
    
    return difference_movies

def get_friends_unique_watched(user_data):
    movies_not_watched_by_user = []
    watched_movies = user_data["watched"]
    friends = user_data["friends"]

    for friend in friends:
        friend_movies = friend["watched"]
        for friend_movie in friend_movies:

            if friend_movie not in watched_movies:
                if friend_movie in movies_not_watched_by_user:
                    continue
                #else:
                movies_not_watched_by_user.append(friend_movie)

    return movies_not_watched_by_user


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data): 
    user_host_recs = []
    friends_list = get_friends_unique_watched(user_data)
    for i in friends_list:
        if i["host"] in user_data["subscriptions"]:
            user_host_recs.append(i)
    return user_host_recs
     

    

    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------