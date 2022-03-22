# ------------- WAVE 1 --------------------
import pytest
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(movie_title, genre, rating):    

    if movie_title == None or genre == None or rating == None:
        return None

    new_movie = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating
    }

    return new_movie

def add_to_watched(user_data, movie):

    list = user_data["watched"]
    list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    watchlist_list = user_data["watchlist"]
    watchlist_list.append(movie)

    return user_data


def watch_movie(user_data, movie):

    watchlist_list = user_data["watchlist"]
    watched_list = user_data["watched"]

    for film in watchlist_list:
        if film['title'] == movie:
            watched_list.append(film)
            watchlist_list.remove(film)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    '''
        USER_DATA_2 = {
        "watched": [
            FANTASY_1, 
            FANTASY_2, 
            FANTASY_3, 
            ACTION_1, 
            INTRIGUE_1, 
            INTRIGUE_2
            ],    
    }

    FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8

    '''

    count_rating = 0
    count_sum_rating = 0

    if not len(user_data["watched"]) == 0:
        for lists in user_data.values():
            for films in lists:
                count_sum_rating += films["rating"]
                count_rating += 1
        
        average = count_sum_rating/count_rating
    else:
        average = len(user_data["watched"])

    return average

'''
The next three tests are about a get_most_watched_genre() function.
In party.py, there should be a function named get_most_watched_genre. This function should...

take one parameter: user_data
the value of user_data will be a dictionary with a "watched" list of movie dictionaries. Each movie dictionary has a key "genre".
This represents that the user has a list of watched movies. Each watched movie has a genre.
The values of "genre" is a string.
Determine which genre is most frequently occurring in the watched list
return the genre that is the most frequently watched
If the value of "watched" is an empty list, get_most_watched_genre should return None.
'''
def get_most_watched_genre(user_data):

    list_of_genre = []
    genre_dict = {}

    if not len(user_data["watched"]) == 0:
        for i in range(len(user_data["watched"])):
            list_of_genre.append(user_data["watched"][i]["genre"])

        for genre in list_of_genre:
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1

        max_value = 0
        popular_genre = ""

        for key,value in genre_dict.items():
            if value > max_value:
                max_value = value
                popular_genre = key
    else:
        popular_genre = None

    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

