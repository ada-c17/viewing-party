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

def get_unique_set_watch_from_user(user_data):

    #creating a set of users unique titles
    user_watch_list = user_data["watched"]
    set_of_users_films = set()
    for values in range(len(user_watch_list)):
        u_films_title = user_watch_list[values]["title"]
        set_of_users_films.add(u_films_title)
    return set_of_users_films

def get_unique_set_watch_from_friends(user_data):

    #creating a set of friends unique titles
    friends_watched_list = user_data["friends"]
    set_of_friends_films = set()
    for values in range(len(friends_watched_list)):
        watched_lists = friends_watched_list[values]["watched"]
        for films in range(len(watched_lists)):
            f_films_title = watched_lists[films]["title"]
            set_of_friends_films.add(f_films_title)
    return set_of_friends_films

def get_unique_watched(user_data):

    # creating sets of unique movies for user and friends
    set_of_users_films = get_unique_set_watch_from_user(user_data)
    set_of_friends_films = get_unique_set_watch_from_friends(user_data)

    # determine which movies the user has watched, but none of their friends have watched
    list_for_suggestion = list(set_of_users_films - set_of_friends_films)

    # return fron list nested list of dictionaries, by key "title" and by value store in 
    # the list_for_suggestion
    dict_list_for_suggestion_by_user = []
    user_watch_list = user_data["watched"]
    for films in range(len(list_for_suggestion)):
        for values in range(len(user_watch_list)):
            if user_watch_list[values]["title"] == list_for_suggestion[films]:
                dict_list_for_suggestion_by_user.append(user_watch_list[values])

    return dict_list_for_suggestion_by_user

def get_friends_unique_watched(user_data):

    # creating sets of unique movies for user and friends
    set_of_users_films = get_unique_set_watch_from_user(user_data)
    set_of_friends_films = get_unique_set_watch_from_friends(user_data)

    # determine which movies the friends has watched, but user did not watched
    list_unique_watched = list(set_of_friends_films - set_of_users_films)

    # return fron list nested list of dictionaries, by key "title" and by value store in 
    # the list_unique_watched

    friends_watched_list = user_data["friends"]
    dict_list_for_suggestion_by_friends = []

    for items in range(len(list_unique_watched)):
        for i in range(len(friends_watched_list)):
            watched_lists = friends_watched_list[i]["watched"]
            for films in range(len(watched_lists)):
                if watched_lists[films]["title"] == list_unique_watched[items]:
                    if not watched_lists[films] in dict_list_for_suggestion_by_friends:
                        dict_list_for_suggestion_by_friends.append(watched_lists[films])

    return dict_list_for_suggestion_by_friends

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

'''
USER_DATA_4 = {
    "watched": [
        FANTASY_1b, 
        FANTASY_2b, 
        FANTASY_3b, 
        ACTION_1b, 
        INTRIGUE_1b, 
        INTRIGUE_2b
        ],  
    "friends":  [
        {
            "watched": [
                FANTASY_1b,
                FANTASY_3b,
                FANTASY_4b,
                HORROR_1b,
            ]
        },
        {
            "watched": [
                FANTASY_1b,
                ACTION_1b,
                INTRIGUE_1b,
                INTRIGUE_3b,
            ]
        }  
    ]
}

USER_DATA_4["subscriptions"] = ["netflix", "hulu"]

'''

def get_available_recs(user_data):

# invoke dict_list_for_suggestion_by_friends from get_friends_unique_watched(user_data) function
    dict_list_for_suggestion_by_friends = get_friends_unique_watched(user_data)


# creating a dictionary films with subscribstions user has
    dict_lists_films_wich_user_subscribe_by_host = []
    for films in range(len(dict_list_for_suggestion_by_friends)):
        for subscriptions in range(len(user_data["subscriptions"])):
            if dict_list_for_suggestion_by_friends[films]["host"] == user_data["subscriptions"][subscriptions]:
                dict_lists_films_wich_user_subscribe_by_host.append(dict_list_for_suggestion_by_friends[films])
    return dict_lists_films_wich_user_subscribe_by_host

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    # movies at least one of the user's friends have watched, but the user has not watched collect in the function: get_friends_unique_watched()
    user_no_watch_list = get_friends_unique_watched(user_data)
    # we are determine popular genre in get_most_watched_genre
    popular_genre = get_most_watched_genre(user_data)

    recomendations_to_user_list = []
    for films in range(len(user_no_watch_list)):
        if user_no_watch_list[films]["genre"] == popular_genre:
            recomendations_to_user_list.append(user_no_watch_list[films])
    return recomendations_to_user_list

def get_rec_from_favorites(user_data):

    # none of the user's friends have watched it from get_unique_watched function
    friend_no_watch_list = get_unique_watched(user_data)

    recomendations_from_user_list = []
    for films in range(len(friend_no_watch_list)):
        for i in range(len(user_data["favorites"])):
            if user_data["favorites"][i] == friend_no_watch_list[films]:
                recomendations_from_user_list.append(user_data["favorites"][i])
    return recomendations_from_user_list