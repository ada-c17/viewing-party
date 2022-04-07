# ------------- WAVE 1 --------------------

from audioop import avg
from sys import argv
import pprint
pp = pprint.PrettyPrinter(indent=4)

def create_movie(movie_title, genre, rating):
    '''
    Create a dictionary that appends key:value pairs 
    3 parameters: string, string, float are the values
    Return dictionary
    '''
    dict = {}
    if movie_title == None or genre == None or rating == None:
        return None 
    else:
        dict["title"] = movie_title
        dict["genre"] = genre
        dict["rating"] = rating

    return dict 


def add_to_watched(user_data, movie):
    '''
    2 parameters: dictionary, dictionary
    Update and return user_data to include watched movies
    '''
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    '''
    2 parameters: dictionary, dictionary
    Update and return user_data to include watchlist movies
    '''
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    '''
    2 parameters: dictionary, string
    Update watchlist to watched and return user_data
    '''
    for i in user_data["watchlist"]: 
        if i["title"] == title:
            user_data["watched"].append(i)
            user_data["watchlist"].remove(i)
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''
    1 parameter: dictionary
    Return the average rating of the movies watched by user
    '''
    movies = user_data["watched"]
    summation = 0

    if len(movies) == 0:
        return 0.0
    
    for movie_dict in movies:
        summation += movie_dict["rating"] 

    return summation / len(movies)


def get_most_watched_genre(user_data):
    '''
    1 parameter: dictionary
    Return most watched genre by the user
    '''
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
    '''
    1 parameter: dictionary
    Return movies that user has watched but friends have not
    '''
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
    '''
    1 parameter: dictionary
    Return movies that at least one friend has watched but user has not
    '''
    movies_not_watched_by_user = []
    watched_movies = user_data["watched"]
    friends = user_data["friends"]

    for friend in friends:
        friend_movies = friend["watched"]
        for friend_movie in friend_movies:

            if friend_movie not in watched_movies:
                if friend_movie in movies_not_watched_by_user:
                    continue
                movies_not_watched_by_user.append(friend_movie)

    return movies_not_watched_by_user


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data): 
    '''
    1 parameter: dictionary
    Return recommended movies if user has not watched and 
    at least one friend has watched and host of movie is also 
    within the user's subscriptions
    '''
    user_host_recs = []
    friends_list = get_friends_unique_watched(user_data)
    for i in friends_list:
        if i["host"] in user_data["subscriptions"]:
            user_host_recs.append(i)
    return user_host_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''
    1 parameter: dictionary
    Return movies that user has not watched but friend has that has
    a genre the same as user's most frequent genre
    '''
    new_recs = []
    most_watched_genre = get_most_watched_genre(user_data)
    #print(most_watched_genre)
    friends_watched = get_friends_unique_watched(user_data)
    #print(friends_watched)
    #for my_movie in most_watched_genre:
    for friend_movie in friends_watched:
        if most_watched_genre == friend_movie["genre"]:
            new_recs.append(friend_movie)
    return new_recs


def get_rec_from_favorites(user_data):
    '''
    1 parameter: dictionary
    Return movies that are in user's favorites and none of
    friends have watched it
    '''
    rec_movies = []
    friends_watched = get_friends_unique_watched(user_data)
    #print(user_data["favorites"])
    for movie in user_data["favorites"]:
        for friend_movie in friends_watched:
            # print("*********MY_MOVIE**********")
            # print(movie)
            # print("*********FRIEND_MOVIE**********")
            # print(friend_movie)
            # print("*********REC_MOVIE**********")
            # print(rec_movies)
            # print()
    
            if movie["title"] == friend_movie["title"]:
                break 
            
        rec_movies.append(movie)
        # print(rec_movies)

    #print(rec_movies)
    return rec_movies