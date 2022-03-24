# ------------- WAVE 1 --------------------

import pytest


def create_movie(title, genre, rating):
    """ Create a dictionary for each movie."""
    new_movie_dict = {}
    new_movie_dict["title"] = title
    new_movie_dict["genre"] = genre
    new_movie_dict["rating"] = rating
    for value in new_movie_dict.values():
        if value == None:
            return None
    return new_movie_dict


def add_to_watched(user_data, movie):
    """Add a movie to the user's Wacthed List."""
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """Add a movie to the user's Watchlist."""
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    """Move a movie from user's Watchlist to Watched List."""
    found_watched_movie = []
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            found_watched_movie = movie
    if found_watched_movie:
        user_data["watched"].append(found_watched_movie)
        user_data["watchlist"].remove(found_watched_movie)
    return user_data

# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """ 
    Returns the average rating for all movie the user has watched.  Returns zero if Watch List is empty
    """
    ratings_list = []
    watched_movies = user_data["watched"]
    for movie in watched_movies:
        new_rating = movie["rating"]
        ratings_list.append(new_rating)
    if ratings_list:
        return sum(ratings_list) / len(ratings_list)
    else:
        return 0


def get_most_watched_genre(user_data):
    """
    Get most watched genre from user's Watched List.  Creates a list of genres watched from User Data then creates a dicitonary to capture each genre and its frequency as a key,value.  Manual counter looks for higher value and returns the key (genre)
    """
    watched_movies = user_data["watched"]
    watched_genres = [movie["genre"] for movie in watched_movies]
    most_watched_genre_dict = {}
    most_watched_genre = ""
    most_watched_counter = 0
    for genre in watched_genres:
        if genre in most_watched_genre_dict:
            most_watched_genre_dict[genre] += 1
        else:
            most_watched_genre_dict[genre] = 1
    for genre in most_watched_genre_dict:
        if most_watched_genre_dict[genre] > most_watched_counter:
            most_watched_genre = genre
            most_watched_counter = most_watched_genre_dict[genre]
    #My code will not capture a tie for most watched genre.  It will just return the first one it enountered.
    if most_watched_counter == 0:
        return None
    return most_watched_genre

# ------------- WAVE 3 -------∫-------------
# -----------------------------------------
def get_unique_watched(user_data):
    """
    Compares users Watched List to all of the friends Wacthed Lists and return a list of movie dictionaries that only the user has watched
    """
    user_watched = user_data["watched"]
    friends_watched_lists = []
    friends_watched = []
    for friend in user_data["friends"]:
        for watched, movies in friend.items():
            friends_watched_lists.append(movies) 
    for each_friends_list in friends_watched_lists:
        for movie in each_friends_list:
            if movie not in friends_watched:
                friends_watched.append(movie) 
    return [movie for movie in user_watched if movie not in friends_watched]


def get_friends_unique_watched(user_data):
    """
    Compares all friend's Watched Lists and return a list of movie dictionaries the user does not have on their Watched List.
    """
    user_watched = user_data["watched"]
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for watched, movies in friend.items():
            for movie in movies:
                if movie not in friends_unique_watched:
                        friends_unique_watched.append(movie)
    return [movie for movie in friends_unique_watched if movie not in user_watched]

    # ------------- WAVE 4 --------------------
    # -----------------------------------------
def get_available_recs(user_data):
    """ 
    Calls get_friends_unique_watched to find movies user hasn't watched that a friend has.  Returns a list of movie dictionaries that only a friend has seen and the movie host is found in the user's subsciptions.
    """
    
    user_watched = user_data["watched"]
    friends_unique_watched = get_friends_unique_watched(user_data)
    
    return [movie for movie in friends_unique_watched if movie["host"] in user_data["subscriptions"]]

    # ------------- WAVE 5 --------------------
    # -----------------------------------------
def get_new_rec_by_genre(user_data):
    """
    Calls most_watched_genre to determine user's most watched genre.  Calls get_friends_unique_watched to create list of movies friends have watched but user has not.  Returns a list of movie dicts that only a friend has seen and matched the users most watched genre.
    """
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    return [movie for movie in friends_unique_watched if movie["genre"] == most_watched_genre]

def get_rec_from_favorites(user_data):
    """
    Calls get_unique_watched to create a list of movie dictionaries the user has watched but none of their friends have seen.  Returns a list of movie dictionaries of movies found in the user's favorite that none of their friends have seen.
    """
    favorites = user_data["favorites"]
    unique_watched = get_unique_watched(user_data)
    
    return [movie for movie in favorites if movie in unique_watched]




