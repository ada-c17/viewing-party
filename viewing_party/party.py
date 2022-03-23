# ------------- WAVE 1 --------------------
import pytest
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(movie_title, genre, rating):    

    if movie_title == None or genre == None or rating == None:
        return None

    new_movie = {}

    new_movie["title"] = movie_title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

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
'''''
The first two tests are about a get_unique_watched() function.
In party.py, there should be a function named get_unique_watched. This function should...

take one parameter: user_data
the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
This represents that the user has a list of watched movies and a list of friends
The value of "friends" is a list
Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
Each movie dictionary has a "title".
Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
Return a list of dictionaries, that represents a list of movies

USER_DATA_3["friends"] =  [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }
    ]  

    FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
'''''

def get_unique_watched(user_data):

#creating a set of users unique titles
    user_watch_list = user_data["watched"]
    set_of_users_films = set()
    for values in range(len(user_watch_list)):
        u_films_title = user_watch_list[values]["title"]
        set_of_users_films.add(u_films_title)

    #creating a set of friends unique titles
    friends_watched_list = user_data["friends"]
    set_of_friends_films = set()
    for values in range(len(friends_watched_list)):
        watched_lists = friends_watched_list[values]["watched"]
        for films in range(len(watched_lists)):
            f_films_title = watched_lists[films]["title"]
            set_of_friends_films.add(f_films_title)

    # determine which movies the user has watched, but none of their friends have watched
    list_for_suggestion = list(set_of_users_films - set_of_friends_films)


    # return a list of dictionaries, that represents a list of movies
    dict_list_for_suggestion = []
    for films in range(len(list_for_suggestion)):
        for values in range(len(user_watch_list)):
            if user_watch_list[values]["title"] == list_for_suggestion[films]:
                dict_list_for_suggestion.append(user_watch_list[values])

    return dict_list_for_suggestion

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

