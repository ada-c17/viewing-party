# ------------- WAVE 1 --------------------

from imp import new_module
from turtle import up
from zoneinfo import available_timezones


def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
        return None
    new_movie['title'] = title
    new_movie['genre'] = genre
    new_movie['rating'] = rating 
    return new_movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    for film in watchlist:
        if film['title'] == movie_title:
            watchlist.remove(film)
            watched.append(film) 
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched = user_data['watched']
    rating_sum = 0

    # if len(watched) != 0:
    #     try:
    #         for movie in watched:
    #             rating_sum  += movie['rating']
    #         rating_avg = rating_sum / len(watched)
    #         return rating_avg
    #     except ZeroDivisionError:
    #         return 0.0
    

    for movie in watched:
        rating_sum  += movie['rating']

    if len(watched) != 0:
        rating_avg = rating_sum / len(watched)
        return rating_avg
    else:
        return 0.0
            

def get_most_watched_genre(user_data):
    watched = user_data['watched']
    all_genres_watched = {}

    if watched == []:
        return None
    else:
        for movie in watched:
            if movie['genre'] in all_genres_watched:
                all_genres_watched[movie['genre']] += 1
            else:
                all_genres_watched[movie['genre']] = 1
        
        max_value = max(all_genres_watched.values())
        popular_genre = [genre for genre, number_watched in all_genres_watched.items() if number_watched == max_value]

        return (', '.join(popular_genre))


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    #returns a list with unique movies watched by user only
    watched_by_user = user_data['watched'] 
    watched_by_friends = get_movies_watched_by_friends(user_data) 
    user_unique_movies = []
    
    for user_movie in watched_by_user: 
        if user_movie not in watched_by_friends and user_movie not in user_unique_movies:
                user_unique_movies.append(user_movie)

    return user_unique_movies

def get_movies_watched_by_friends(user_data):
    #returns a list with all friends' watched movies
    watched_by_friends = [] 

    for friends in user_data['friends']:
        for movies in friends.values():
            for movie in movies:
                watched_by_friends.append(movie)
    return watched_by_friends

def get_friends_unique_watched(user_data):
    #returns a list with unique movies watched by friends only
    watched_by_user = user_data['watched'] 
    watched_by_friends = get_movies_watched_by_friends(user_data) 
    friends_unique_movies = []

    for movie in watched_by_friends:
        if movie not in watched_by_user and movie not in friends_unique_movies:
            friends_unique_movies.append(movie)
    
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    #returns a list of recommended films that user hasn't watched 
    #and has a subscription to the service where movie is streamed.
    user_subscriptions = user_data['subscriptions']
    all_recommendations = get_friends_unique_watched(user_data)
    available_recommendation = []
    
    for recommendation in all_recommendations:
        if recommendation['host'] in user_subscriptions:
            available_recommendation.append(recommendation)
    
    return available_recommendation

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
