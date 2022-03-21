

# ------------- WAVE 1 --------------------

from pyparsing import empty


def create_movie(title, genre, rating):
    # creating a dictionary that stores the variables passed into the function as the values
    new_movie_added = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # checks to make sure that the variables passed into the function are real values and not none. If none, returns none. If valid input, then returns the dict.
    if title is None or genre is None or rating is None:
        return None
    else:
        return new_movie_added

def add_to_watched(user_data, movie):
    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in watched_movies 
    if not user_data:
        return user_data
    else:
        user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in movies_to_watch dictionary
    if not user_data:
        return user_data
    else:
        user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, title):   
    for i in range(len(user_data["watchlist"])): # loops through all_movies["watchlist"] 
        if title in user_data["watchlist"][i]["title"]: # conditional that checks if the title is in the all_movies["watchlist"] at index i 
            user_data["watchlist"].remove(user_data["watchlist"][i]) # removes the title from the all_movies["watchlist"]  at index i 
            user_data["watched"].append(title) # adds the title to the all_movies["watched"] 

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_list = []
    empty_list_rating = 0.0

    for item in user_data["watched"]: # loops through all items in "watched"
        ratings_list.append(item["rating"]) # adds the ratings from "watched" to ratings_list
    
    if len(user_data["watched"]) != 0:
        movie_ratings_average = sum(ratings_list) / len(ratings_list)
    else:
        return empty_list_rating # returns 0.0
    
    return movie_ratings_average # returns if finished with average calculation 

def get_most_watched_genre(user_data):
    genre_list = []

    for item in user_data["watched"]: # loops through list
        genre_list.append(item["genre"]) # appends values of "genre" key to genre_list dictionary

    if len(user_data["watched"]) != 0:
        genre_list.sort() # sorts list in place (modifies original list)
        most_common_genre = max(genre_list, key = genre_list.count) # uses the max function to find the most common genre in genre_list with list.count function to count the occurences
    else:
        return None 
    
    return most_common_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched_movies = []
    friends_watched_movies = []

    for item in user_data ["watched"]:
        user_watched_movies.append(item)
    
    for i in range(len(user_data ["friends"])):
        for item in user_data["friends"][i]["watched"]: 
            friends_watched_movies.append(item)

    unique_user_movies = [item for item in user_watched_movies if item not in friends_watched_movies] # list comprehension that stores all movie titles not in friends_watched_movies
    
    return unique_user_movies

def get_friends_unique_watched(user_data): 
    user_watched_movies = []
    friends_watched_movies = []
    unique_friend_movies = []


    for item in user_data ["watched"]:
        user_watched_movies.append(item)
    
    for i in range(len(user_data["friends"])):
        for item in user_data["friends"][i]["watched"]: 
            friends_watched_movies.append(item)

    friend_movies_list = [item for item in friends_watched_movies if item not in user_watched_movies] # list comprehension that stores all movie titles not in friends_watched_movies
    for item in friend_movies_list:
        if item not in unique_friend_movies:
            unique_friend_movies.append(item)

    return unique_friend_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_watched_movies = []
    friends_watched_movies= []
    user_movie_recs = []

    for item in user_data["watched"]:
        user_watched_movies.append(item)
    
    for i in range(len(user_data["friends"])):
        for item in user_data ["friends"][i]["watched"]: 
            friends_watched_movies.append(item)

    movie_recs = [item for item in friends_watched_movies if item not in user_watched_movies] # list comprehension that stores all movie titles not in friends_watched_movies
    for i in range(len(user_data)- 1):
        if movie_recs[i]["host"] not in user_data["subscriptions"][i]:
            user_movie_recs.append(movie_recs[i])

    return user_movie_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

