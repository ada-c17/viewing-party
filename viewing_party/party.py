# ------------- WAVE 1 --------------------

from curses import keyname
from lib2to3.pgen2.tokenize import generate_tokens
from operator import itemgetter
from xml.sax.handler import EntityResolver

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1, USER_DATA_2

# adds movie data as item in movie dictionary
def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else: 
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
    }
    return movie

# adds movie to watched list
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

# adds movie to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

# moves watchlist movie to watched list
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        for category, item in movie.items():
            if category == "title" and item == title:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# gets average rating of movies for user
def get_watched_avg_rating(user_data):
    ratings = []
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]: 
            for category, item in movie.items():
                if category == "rating":
                    ratings.append(item)   
        average_rating = ((sum(ratings))/(len(ratings)))
    else:
        average_rating = 0
    return average_rating

# returns most watched genre in user's movies
def get_most_watched_genre(user_data):
    genres = {}
    if user_data["watched"]:
        for movie in user_data["watched"]: 
            for category, item in movie.items():
                if category == "genre":
                    if item not in genres:
                        genres[item] = 0
                    else:
                        genres[item] += 1
        popular_genre = (max(genres, key=genres.get))
        return popular_genre
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# returns unique movie list from user's movies
def get_unique_watched(user_data):
    unique_watched = []
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    friend_movies = []
    for friend in friends: # loops through friend 0 and friend 1
        friend_movies += friend["watched"] #assigns list
    for user_movie in user_watched: #gets the first user movie
        if user_movie not in friend_movies:
                if user_movie not in unique_watched:
                    unique_watched.append(user_movie)
    return unique_watched

# returns unique friends movie list from friends' movies
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    friend_movies = []
    for friend in friends: # loops through friend 0 and friend 1
        for friend_movie in friend:
            if friend_movie not in friend_movies:
                friend_movies += friend["watched"] #assigns list
    
    for friend_movie in friend_movies:
        if friend_movie not in user_watched:
                if friend_movie not in friends_unique_watched:
                    friends_unique_watched.append(friend_movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# returns recommendations list from friends' movie list
# movies from friends' list are unwatched by user and have host that is in user subscriptions
def get_available_recs(user_data):
    recommendations = []
    unique_watched = get_unique_watched(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    if "subscriptions" in user_data:
        for friend_movie in friends_unique_watched:
            if friend_movie not in unique_watched:
                if friend_movie["host"] in user_data["subscriptions"]:
                    recommendations.append(friend_movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# return recommendations list from friends' movie list
# for movies matching user's favorite genre
def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    favorite_genre = get_most_watched_genre(user_data)
    recommendations = get_available_recs(user_data)
    for friend_movie in recommendations:
        if friend_movie["genre"] == favorite_genre:
            if friend_movie not in recs_by_genre:
                recs_by_genre.append(friend_movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    recommendations = []
    user_favorites = user_data["favorites"]
    friends = user_data["friends"]
    friend_movies = []
    for friend in friends: # loops through friend 0 and friend 1
        friend_movies += friend["watched"] #assigns list
    for user_movie in user_favorites: #gets the first user movie
        if user_movie not in friend_movies:
                if user_movie not in recommendations:
                    recommendations.append(user_movie)
    return recommendations
# -----------------------------------------