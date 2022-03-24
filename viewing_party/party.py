# ------------- WAVE 1 --------------------

from collections import Counter


def create_movie(title, genre, rating):

    if title and genre and rating:
    
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
            }
        return movie
    
    else:
        return None
    
def add_to_watched(user_data, movie):
    
    watched = []

    user_data = {"watched": watched}

    for value in user_data.values():
        watched.append(movie)
                
    return user_data

def add_to_watchlist(user_data, movie):

    watchlist = []

    user_data = {"watchlist": watchlist}

    for value in user_data.values():
        watchlist.append(movie)

    return user_data

def watch_movie(user_data, title):

    for i in range(len(user_data["watchlist"])):
        if (user_data["watchlist"][i]["title"]) == title:
            watched_movie = user_data["watchlist"].pop(i)

            for value in user_data.values():
                user_data["watched"].append(watched_movie)
                return user_data

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):

    ratings_list = []

    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    
    if ratings_list == []:
        return 0
    else: 
        return sum(ratings_list) / len(ratings_list)

def get_most_watched_genre(user_data):

    genre_list = []

    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    if genre_list == []:
        return None
    
    else:
        genre_frequency = Counter(genre_list)
        most_common_genre_frequency = genre_frequency.most_common(1)
        most_common_genre = most_common_genre_frequency[0][0]
        return most_common_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_compiled_watched_set = set()
    friends_unique_compiled_set = set()

    for movie in user_data["watched"]:
        user_compiled_watched_set.add(tuple(movie.items()))

    for i in range(len(user_data["friends"])):
            for watched in user_data["friends"][i].values():
                for movie in watched:
                    friends_unique_compiled_set.add(tuple(movie.items()))

    user_but_not_friends = user_compiled_watched_set.difference(friends_unique_compiled_set)

    movies_user_has_watched_but_friends_have_not = []

    for tup in user_but_not_friends:
        user_but_not_friends_dict_type = dict(tup)
        movies_user_has_watched_but_friends_have_not.append(user_but_not_friends_dict_type)
        
    return movies_user_has_watched_but_friends_have_not

def get_friends_unique_watched(user_data):

    user_compiled_watched_set = set()
    friends_unique_compiled_set = set()

    for movie in user_data["watched"]:
        user_compiled_watched_set.add(tuple(movie.items()))

    for i in range(len(user_data["friends"])):
            for watched in user_data["friends"][i].values():
                for movie in watched:
                    friends_unique_compiled_set.add(tuple(movie.items()))

    friends_but_not_user = friends_unique_compiled_set.difference(user_compiled_watched_set)

    movies_friends_have_but_user_has_not = []

    for tup in friends_but_not_user:
        friends_but_not_user_dict_type = dict(tup)
        movies_friends_have_but_user_has_not.append(friends_but_not_user_dict_type)
        
    return movies_friends_have_but_user_has_not


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    movie_recommended_by_friends = get_friends_unique_watched(user_data)

    recommended_movie_list = []

    for movie in movie_recommended_by_friends:
        for key, value in movie.items():
            if key == "host":
                if value in user_data["subscriptions"]:
                    recommended_movie_list.append(movie)

    return(recommended_movie_list)


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    movie_recommended_by_friends = get_friends_unique_watched(user_data)

    user_most_frequent_genre = get_most_watched_genre(user_data)

    recommended_movie_list_by_genre = []

    for movie in movie_recommended_by_friends:
        for key, value in movie.items():
            if key == "genre":
                if value == user_most_frequent_genre:
                    recommended_movie_list_by_genre.append(movie)

    return recommended_movie_list_by_genre

def get_rec_from_favorites(user_data):

    user_watched_movies = get_unique_watched(user_data)

    user_favorites = user_data["favorites"]

    user_watched_movies_set = set()
    user_favorite_movies_set = set()

    for movie in user_watched_movies:
        user_watched_movies_set.add(tuple(movie.items()))

    for movie in user_data["favorites"]:
        user_favorite_movies_set.add(tuple(movie.items()))

    user_watched_favorites = user_favorite_movies_set.intersection(user_watched_movies_set)

    recommended_movie_list_from_favorites = []

    for tup in user_watched_favorites:
        user_watched_favorites_dict_type = dict(tup)
        recommended_movie_list_from_favorites.append(user_watched_favorites_dict_type)
        
    return recommended_movie_list_from_favorites
