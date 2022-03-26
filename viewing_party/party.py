# ------------- WAVE 1 --------------------

from enum import unique

# This is a helper function used in some above functions
def get_users_watched_movie_titles(user_data):
    users_watched_movies = []
    for film in user_data["watched"]:
        users_watched_movies.append(film["title"])
    return users_watched_movies

def create_movie(title, genre, rating):
    movie = {"title" : title, "genre" : genre, "rating" : rating}
    
    if not title or not genre or not rating: 
        movie = None
    
    return movie

def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    
    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, movie_title):
    
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    movie_counter = 0
    rating_total = 0

    for movie in user_data["watched"]:
        movie_counter += 1
        rating_total += movie["rating"]
    if movie_counter == 0:
        average_rating = 0.0
    else: 
        average_rating = rating_total / movie_counter
    
    return average_rating

def get_most_watched_genre(user_data):
    
    if not user_data["watched"]:
        return None
    else: 
        genre_dict = {}
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1
        
        popular_genre = max(genre_dict, key=genre_dict.get)
        print(genre_dict)
        return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = []
    friend_watched_movies = []

    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            friend_watched_movies.append(movie["title"])

    for film in user_data["watched"]:
        if film ["title"] not in friend_watched_movies:
            unique_movies.append(film)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies= []
    users_watched_movies = get_users_watched_movie_titles(user_data)
    
    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            if movie["title"] not in users_watched_movies\
                and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    
    return friends_unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    users_watched_movies = get_users_watched_movie_titles(user_data)

    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            if movie["title"] not in users_watched_movies\
            and movie["host"] in user_data["subscriptions"]:
                recommended_movies.append(movie)

    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies_by_genre = []
    users_watched_movies = get_users_watched_movie_titles(user_data)

    fav_genre = get_most_watched_genre(user_data)  

    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            if movie["title"] not in users_watched_movies\
            and movie["genre"] == fav_genre:
                recommended_movies_by_genre.append(movie)
    
    return recommended_movies_by_genre

def get_rec_from_favorites (user_data): 
    recommended_movies_from_favorites = []
    friends_watched_movies = []
    
    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            friends_watched_movies.append(movie["title"])
    
    for film in user_data["favorites"]:
        if film["title"] not in friends_watched_movies:
            recommended_movies_from_favorites.append(film)
    
    return recommended_movies_from_favorites

