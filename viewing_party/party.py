

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
    # creating variable that stores user_data
    watched_movies = user_data
    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in watched_movies 
    if not watched_movies:
        return watched_movies
    else:
        watched_movies["watched"].append(movie)
    
    return watched_movies

def add_to_watchlist(user_data, movie):
    movies_to_watch = user_data

    # checks to see if list is empty, if it is empty, it returns empty list. If not empty, continues with conditional and appends movie dictionary to value in movies_to_watch dictionary
    if not movies_to_watch:
        return movies_to_watch
    else:
        movies_to_watch["watchlist"].append(movie)
    
    return movies_to_watch

def watch_movie(user_data, title):
    # stores user_data in all_movies variable
    all_movies = user_data
    
    for i in range(len(all_movies["watchlist"])): # loops through all_movies["watchlist"] 
        if title in all_movies["watchlist"][i]["title"]: # conditional that checks if the title is in the all_movies["watchlist"] at index i 
            all_movies["watchlist"].remove(all_movies["watchlist"][i]) # removes the title from the all_movies["watchlist"]  at index i 
            all_movies["watched"].append(title) # adds the title to the all_movies["watched"] 

    return all_movies


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    movie_ratings = user_data
    ratings_list = []
    empty_list_rating = 0.0

    for item in movie_ratings["watched"]: # loops through all items in "watched"
        ratings_list.append(item["rating"]) # adds the ratings from "watched" to ratings_list
    
    if len(movie_ratings["watched"]) != 0:
        movie_ratings_average = sum(ratings_list) / len(ratings_list)
    else:
        return empty_list_rating # returns 0.0
    
    return movie_ratings_average # returns if finished with average calculation 

def get_most_watched_genre(user_data):
    movie_genre = user_data
    genre_list = []

    for item in movie_genre["watched"]: # loops through list
        genre_list.append(item["genre"]) # appends values of "genre" key to genre_list dictionary

    if len(movie_genre["watched"]) != 0:
        genre_list.sort() # sorts list in place (modifies original list)
        most_common_genre = max(genre_list, key = genre_list.count) # uses the max function to find the most common genre in genre_list with list.count function to count the occurences
    else:
        return None 
    
    return most_common_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched = user_data 
    user_watched_movies = []
    friends_watched_movies = []

    for item in user_watched["watched"]:
        user_watched_movies.append(item)
    
    for i in range(len(user_watched["friends"])):
        for item in user_watched["friends"][i]["watched"]: 
            friends_watched_movies.append(item)

    unique_user_movies = [item for item in user_watched_movies if item not in friends_watched_movies] # list comprehension that stores all movie titles not in friends_watched_movies
    
    return unique_user_movies

def get_friends_unique_watched(user_data): 
    user_watched = user_data 
    user_watched_movies = []
    friends_watched_movies = []
    unique_friend_movies = []


    for item in user_watched["watched"]:
        user_watched_movies.append(item)
    
    for i in range(len(user_watched["friends"])):
        for item in user_watched["friends"][i]["watched"]: 
            friends_watched_movies.append(item)

    friend_movies = [item for item in friends_watched_movies if item not in user_watched_movies] # list comprehension that stores all movie titles not in friends_watched_movies
    for item in friend_movies:
        if item not in unique_friend_movies:
            unique_friend_movies.append(item)

    return unique_friend_movies


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

