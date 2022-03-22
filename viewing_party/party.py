# ------------- WAVE 1 --------------------

import pytest


def create_movie(title, genre, rating):
    new_movie_dict = {}
    new_movie_dict["title"] = title
    new_movie_dict["genre"] = genre
    new_movie_dict["rating"] = rating
    for value in new_movie_dict.values():
        if value == None:
            return None
    return new_movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            found_watched_movie = movie
            user_data["watched"].append(found_watched_movie)
            index = watchlist.index(movie)
            user_data["watchlist"].pop(index)
    return user_data


# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
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
    if most_watched_counter == 0:
        return None
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 -------∫-------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_list = user_data["friends"]
    friends_watched_lists = []
    friends_watched = []
    for friend in friends_list:
        for watched, movies in friend.items():
            friends_watched_lists.append(movies)
    for group in friends_watched_lists:
        for movie in group:
            friends_watched.append(movie)
    unique = [movie for movie in user_watched if movie not in friends_watched]
    return unique

def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for watched, movies in friend.items():
            if watched == "watched":
                for movie in movies:
                    if movie not in friends_unique_watched:
                        friends_unique_watched.append(movie)
    return [movie for movie in friends_unique_watched if movie not in user_watched]

    



    #
    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------
    # -----------------------------------------
    # ------------- WAVE 5 --------------------
    # -----------------------------------------


FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}
HORROR_1 = {
    "title": "Scream",
    "genre": "Horror",
    "rating": 3.5
}

INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}


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
USER_DATA_2["friends"] = [
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

get_friends_unique_watched(USER_DATA_2)
