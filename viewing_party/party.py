import statistics
from statistics import mode

# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            movie_dict = user_data["watchlist"].pop(i)
            user_data["watched"].append(movie_dict)
    return user_data

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    ratings = [] # Initialize list that will store all ratings 
    watched_list = user_data["watched"] # Extract the watched list from the rest of the user data
    
    for movie in watched_list: # Iterate through the watched list
        ratings.append(movie["rating"]) # Add each movies rating to ratings list

    ratings_sum = 0.0
    for rating in ratings:
        ratings_sum += rating
    
    if ratings_sum != 0: # Calculates avg if ratings sum is not zero
        avg_rating = ratings_sum / len(ratings)
    else:
        return 0.0
    return avg_rating

def get_most_watched_genre(user_data):
    genres = [] # List will hold every instance of a genre in user watched list
    watched_list = user_data["watched"] # Extract watched list from rest of user data

    for movie in watched_list:
        genres.append(movie["genre"])

    return mode(genres)
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

