# ------------- WAVE 1 --------------------

from time import monotonic


def create_movie(title, genre, rating):
    movie_dict = {}

    if title and genre and rating:
        movie_dict['title'] = title 
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for i in user_data['watchlist']:
        if i['title'] == movie:
            user_data['watched'].append(i)
            user_data['watchlist'].remove(i)    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_total = 0
    counter = 0
    for i in user_data['watched']:
        rating_total += i['rating']
        counter += 1

    if rating_total >0:
        avg_rating = rating_total/counter
    else:
        avg_rating = 0
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []
    for i in user_data['watched']:
        genre_list.append(i['genre'])
    if genre_list:
        return max(set(genre_list), key = genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_movies = []
    friends_movies = []
    user_unique_movies = []

    for i in user_data['watched']:
        user_movies.append(i)

    for i in user_data['friends']:
        for x in i['watched']:
            friends_movies.append(x)

    for i in user_movies:
        if i not in friends_movies and i not in user_unique_movies:
            user_unique_movies.append(i) 
    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_movies = []
    friends_movies = []
    friends_unique_movies = []

    for i in user_data['watched']:
        user_movies.append(i)

    for i in user_data['friends']:
        for x in i['watched']:
            friends_movies.append(x)

    for i in friends_movies:
        if i not in user_movies and i not in friends_unique_movies:
            friends_unique_movies.append(i) 
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_subscriptions = user_data['subscriptions']
    user_recommendations = []
    friends_watched = []

    for dicts in user_data['friends']:
        for movie in dicts['watched']:
            friends_watched.append(movie)

    for i in friends_watched:
        if i['host'] in user_subscriptions:
            if i not in user_data['watched'] and i not in user_recommendations:
                user_recommendations.append(i)

    return user_recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_most_watched = get_most_watched_genre(user_data)
    friends_watched = []
    most_genre_recommendations = []

    for dicts in user_data['friends']:
        for movie in dicts['watched']:
            friends_watched.append(movie)

    for i in friends_watched:
        if i not in user_data['watched']:
            if i['genre'] == genre_most_watched:
                most_genre_recommendations.append(i)

    return most_genre_recommendations
# need to go back to wave 3 assert tests to add in a few more assertions
