# ------------- WAVE 1 --------------------

from collections import UserString
from enum import unique
from re import U


def create_movie(title, genre, rating):
    if not(title and genre and rating):
        return None

    movie = {}
    
    movie['title'] = title
    movie['genre'] = genre
    movie['rating'] = rating

    return movie 

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    movie_watched = None

    for movie in user_data['watchlist']:
        if movie['title'] == movie_title:
            movie_watched = movie
            break
            
    if movie_watched:
        user_data['watched'].append(movie_watched)
        user_data['watchlist'].remove(movie_watched)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0
    average_rating = 0.0

    if user_data['watched']:
        # find the number of movies and add all ratings together
        for movie in user_data['watched']:
            # num_movies += 1
            total_ratings += movie['rating']
        average_rating = total_ratings / len(user_data['watched'])
    
    return average_rating

def get_most_watched_genre(user_data):
    genre_counts = {}
    most_watched_genre = None

    if user_data['watched']:
        # create dictionary with genre as key and frequency of genre as value
        for movie in user_data["watched"]:
            if movie['genre'] not in genre_counts:
                genre_counts[movie['genre']] = 1
            elif movie['genre'] in genre_counts:
                genre_counts[movie['genre']] += 1
        #use max to get the key with highest frequency from dictionary
        most_watched_genre = max(genre_counts, key=genre_counts.get)

    return most_watched_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# helper function to combine friends movies into a single list, removing duplicates
def combine_friends_movies(user_data):
    friends_movies = []

    if 'friends' not in user_data:
        return friends_movies

    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friends_movies:
                friends_movies.append(movie)
            
    return friends_movies

def get_unique_watched(user_data):
    unique_movies = []

    friends_movies = combine_friends_movies(user_data)

    # compare user watched movies to friends to find unique movies
    for movie in user_data['watched']:
        if movie not in friends_movies and movie not in unique_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = combine_friends_movies(user_data)
    friends_unique_movies = []
    
    # loop through user's data to find friend's unique movies
    for movie in friends_movies:
        if movie not in user_data['watched']:
            friends_unique_movies.append(movie)

    return friends_unique_movies 

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []

    if 'subscriptions'not in user_data:
        return recommended_movies

    movies_not_watched = get_friends_unique_watched(user_data)
    # add movies user hasn't seen but are available on their subscribed streaming services
    for movie in movies_not_watched:
        if movie['host'] in user_data['subscriptions']:
            recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_recommendations = []
    all_recommendations = get_available_recs(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    for movie in all_recommendations:
        if movie['genre'] == most_watched_genre:
            genre_recommendations.append(movie)

    return genre_recommendations

def get_rec_from_favorites(user_data):
    possible_recommendations = get_unique_watched(user_data)
    recommendations_from_favorites = []

    for movie in possible_recommendations:
        if movie in user_data['favorites']:
            recommendations_from_favorites.append(movie)
            
    return recommendations_from_favorites