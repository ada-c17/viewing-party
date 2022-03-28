# ------------- WAVE 1 --------------------


## Create a function that will create a movie function
# with title, genre, and rating into a dictiionary
# If there is no title, genre, or rating, return None
# If any of the three variables is missing, return None

from decimal import DivisionByZero
from tests.test_constants import USER_DATA_2


def create_movie(title, genre, rating):

    if not title or not genre or not rating:
        return None
    else: 
        new_movie = {
            "genre" : genre, 
            "rating": rating,
            "title" : title,
        }
    return new_movie


## Create a function to track when movies are watched
## use the new_movie list to generate how the function works
## user_data is what has been "watched:"
## updated_data = add_to_watched(user_data, movie)

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


## Create a function to track a watch list for the user
## user_data = {"watchlist"}
## updated_data = add_to_watchlist(user_data, movie)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

## def a function that will call upon the watched and watchlist functions
##  adjust the values of watched and watchlist into sets
## use set functions to create a set that compares the similarities
## return a set or dictionary that outputs the difference 
## Return an error message if the movie is on neither list

def watch_movie(user_data, title):  
    for movies in user_data["watchlist"]:
        if movies["title"] == title: 
            user_data["watchlist"].remove(movies)
            user_data["watched"].append(movies)
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
## Create a function that will check the average rating of movies watched
## if average is Zero, return error message

'''
input: a dictionary called 'user_data' with a 'watched' list of
movie dictionaries (movies that user has watched)
-- Calculate average rating of all movies user has watched
-- An empty watch list has an average rating of 0.0
output: the average rating
# {   'watched': [   {   'genre': 'Fantasy',
#                        'rating': 4.8,
#                        'title': 'The Lord of the Functions: The Fellowship of '
#                                 'the Function'},
#                    {   'genre': 'Fantasy',
#                        'rating': 4.0,
#                        'title': 'The Lord of the Functions: The Two '
#                                 'Parameters'},
#                    {   'genre': 'Fantasy',
#                        'rating': 4.0,
#                        'title': 'The Lord of the Functions: The Return of the '
#                                 'Value'},
#                    {   'genre': 'Action',
#                        'rating': 2.2,
#                        'title': 'The JavaScript and the React'},
#                    {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
#                    {   'genre': 'Intrigue',
#                        'rating': 4.5,
#                        'title': 'Instructor Student TA Manager'}]}
'''

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"] ## array of dictionaries
    total_rating = []
    counter = 0 
## for a dictionary in the list of movies
    for movie_data in watched_movies:
        v = movie_data["rating"]
        total_rating.append(v)
    if len(total_rating) == 0:
        return 0.0
    average = sum(total_rating) / len(total_rating)
    return average



## def function to track most watched genre
## COUNT of times genre appears
## If there is no amount, return error message
# '''
# input: take in the parameter 'user_data' : a nested dictionary 
# with a VALUE 'watched' list of movie dictionaries
# each movie has the KEY "genre"
# >> this VALUE represents user's list of watched movies
# >> each watched movie contains a genre
# >>>> the VALUES of  KEY "genre" is a string
# create a COUNTER to count which "genre" occurs most often
# If the value of "watched" is empty, return None

# output: The string of the genre that is most frequently watched,
# if value of watched is an empty list could try ... else none

# '''

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    popular_genre = []
    count = 0

    if watched_movies == []:
        return None
    for movie_data in watched_movies: 
        popular_genre.append(movie_data["genre"])
    for movie_data in watched_movies: 
        if count < popular_genre.count(movie_data["genre"]):
            count = popular_genre.count(movie_data["genre"])
    return popular_genre[0]
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched_movies = user_data["watched"]
    friends_list = user_data["friends"]
    user_watched = []
    dictionary_friend_movies = []
    unique_user_movies = [] 

    for movie_watched in friends_list:
        for movie in movie_watched["watched"]:
            dictionary_friend_movies.append(movie)
    for movie in watched_movies:
        user_watched.append(movie)
        if movie not in dictionary_friend_movies:
            unique_user_movies.append(movie)
    return unique_user_movies



def get_friends_unique_watched(user_data):
    watched_movies = user_data["watched"]
    friends_list = user_data["friends"]
    unique_friend_movies = [] 
    unique_unique = []

    for movie_watched in friends_list: # {} in [{}]
        for movie in movie_watched["watched"]: 
            if movie not in unique_friend_movies:
                unique_friend_movies.append(movie)
                if movie in unique_friend_movies and movie not in watched_movies:
                    unique_unique.append(movie)

    return unique_unique
        


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    movie_rec = []
    watched_movies = user_data["watched"]
    unique_movie_friends = get_friends_unique_watched(user_data)
    user_subscriptions = user_data["subscriptions"]

    for movie in unique_movie_friends:
        if movie["host"] in user_subscriptions and movie not in watched_movies:
            movie_rec.append(movie)
    return movie_rec



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    popular_genre = get_most_watched_genre(user_data)
    unique_movie_friends = get_friends_unique_watched(user_data)
    rec_by_genre = []

    for movie in unique_movie_friends:
        if movie["genre"] == popular_genre:
            rec_by_genre.append(movie)
    return rec_by_genre


def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    friends_list = user_data["friends"]
    friend_watched = []
    rec_by_fave = []

    for movie in friends_list:
        for watched_movie in movie["watched"]:
           friend_watched.append(watched_movie)

    for movie in user_favorites:
        if movie in user_favorites and movie not in friend_watched:
            rec_by_fave.append(movie)
    return rec_by_fave