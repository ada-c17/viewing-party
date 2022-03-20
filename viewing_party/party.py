# ------------- WAVE 1 --------------------

from imp import new_module
from turtle import up


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


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------