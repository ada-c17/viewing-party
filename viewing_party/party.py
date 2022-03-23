

# ------------- WAVE 1 --------------------

from pyparsing import empty

def create_movie(title, genre, rating):
    # creating a dictionary that stores the variables passed into the function as the values
    new_movie_added = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # checks to make sure that the variables passed into the function are real values and not none. 
    # If none, returns none. If valid input, then returns the dict.
    if title is None or genre is None or rating is None:
        return None
    else:
        return new_movie_added

def add_to_watched(user_data, movie):
    # checks to see if list is empty, if it is empty, it returns empty list. 
    # If not empty, continues with conditional and appends movie dictionary to value in watched_movies 
    if not user_data:
        return user_data
    else:
        user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    # checks to see if list is empty, if it is empty, it returns empty list. 
    # If not empty, continues with conditional and appends movie dictionary to value in movies_to_watch dictionary
    if not user_data:
        return user_data
    else:
        user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, title):   
    for movie in range(len(user_data["watchlist"])): # loops through user_data["watchlist"] 
        if title in user_data["watchlist"][movie]["title"]: # conditional that checks if the title is in the user_data["watchlist"] at index i 
            user_data["watchlist"].remove(user_data["watchlist"][movie]) # removes the title from the user_data["watchlist"]  at index i 
            user_data["watched"].append(title) # adds the title to the user_data["watched"] 

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # initialize list object that will store all movie ratings from user_data["watched"]
    user_movie_ratings = []
    # inititalize float variable that stores ratings for empty lists 
    empty_list_rating = 0.0

    for movie in user_data["watched"]: # loops through movies in "watched"
        user_movie_ratings.append(movie["rating"]) # adds the ratings from "watched" to ratings_list
    
    if len(user_data["watched"]) != 0: # if list contains elements and is not equal to 0
        # calculates average by dividing the sum of the list with the length of the list
        movie_ratings_average = sum(user_movie_ratings) / len(user_movie_ratings) 
    else:
        return empty_list_rating # returns 0.0
    
    return movie_ratings_average 

def get_most_watched_genre(user_data):
    # initialize list object that will store the genres of all the movies in user_data["watched"]
    user_movie_genre = []

    for movie in user_data["watched"]: # loops through movie in user_data["watched"] list 
        user_movie_genre.append(movie["genre"]) # appends values of "genre" key to user_movie_genre list

    if len(user_data["watched"]) != 0: # if the list contains elements and is greater than 0 
        user_movie_genre.sort() # sorts list in place (modifies original list)
        # uses the max function to find the most common genre in genre_list with list.count function to count the occurences
        most_common_user_genre = max(user_movie_genre, key = user_movie_genre.count)
    else:
        return None # if list is empty
    
    return most_common_user_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # initialize list object to store movies that both user and friends have watched
    both_watched_movies = []

    for movies in user_data["friends"]: # loops through movies in user_data["friends"]
        for friend_movies in movies["watched"]: # loops through movies in user_data["friends"]["watched"]
            if friend_movies in user_data["watched"]: # conditional that checks if movies that friends have seen are in user_data["watched"] list
                both_watched_movies.append(friend_movies) # adds to list if both friends and user have seen the movie
    # list comprehension that creates new list object that stores movies that only the user has watched 
    unique_user_movies = [movie for movie in user_data["watched"] if movie not in both_watched_movies]

    return unique_user_movies


def get_friends_unique_watched(user_data): 
    # initialize list object to store movies that user has not seen
    user_not_watched_movies = []
    # initialize list object to store movies only friends have seen without duplicates 
    unique_friend_movies = []

    for movies in user_data["friends"]: # loops through movies in user_data["friends"]
        for friends_watched in movies["watched"]: # loops through movies in user_data["friends"]["watched"]
            if friends_watched not in user_data["watched"]: # conditional that checks if movies that friends have seen are not in user_data["watched"] list
                user_not_watched_movies.append(friends_watched) # adds to list if user has not seen the movie, but the friends have
    
    for movie in user_not_watched_movies: # loops through movies in user_not_watched_movies list
        if movie not in unique_friend_movies: # conditional that checks if movie is not (already) in unique_friend_movies - checks for duplicates
            unique_friend_movies.append(movie) # if the movie is not present in unique_friend_movies list, it adds that movie 
    
    return unique_friend_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # initialize list object that will store movie recommedations from user_data["friends"] if available through user_data["subscriptions"]
    movie_recs_by_subs = []

    for friend in user_data["friends"]: # loops through each friend in user_data["friends"] list
        for movie in friend["watched"]: # loops through each movie in friend["watched"]
            # conditional that checks that movie is not in user_data["watched"] list and the "host" in user_data["friends"] matches "subscription" in user_data
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                movie_recs_by_subs.append(movie) # adds movie to list 

    return movie_recs_by_subs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # uses friend_unique_movies function to get movies that only friends have watched 
    friend_unique_movies = get_friends_unique_watched(user_data)
    # uses get_most_watched_genre function to get most common genre and stores that in most_freq_data variable
    most_freq_genre = get_most_watched_genre(user_data) 
    # list comprehension where a list object is created that contains movies that have only been watched by friends and matches users most frequent genre
    movie_recs_by_genre = [movie for movie in friend_unique_movies if movie["genre"] == most_freq_genre]

    return movie_recs_by_genre

def get_rec_from_favorites(user_data): 
    # uses get_unique_watched function to return movies only watched by user and stores it in user_unique_movies variable
    user_unique_movies = get_unique_watched(user_data)

    # list comprehension where a list object is created that contains movies that are both in the user_unique_movies list and the user_data["favorites"] list
    user_movie_favorite_recs = [movie for movie in user_data["favorites"] if movie in user_unique_movies ]

    return user_movie_favorite_recs
    
    
