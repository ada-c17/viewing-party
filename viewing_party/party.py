
from collections import Counter


# ------------- WAVE 1 --------------------


# create_movie_function takes in three parameters (title, genre, rating) and returns a dictionary called movie. 
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

    
# add_to_watched function takes in two parameters (user_data, movie) and creates a list of movies watched by the user.
def add_to_watched(user_data, movie):
    
    watched = []

    user_data = {"watched": watched}

    for value in user_data.values():
        watched.append(movie)
                
    return user_data


# add_to_watchlist function takes in two parameters (user_data, movie) and creates a list of movies to be watched by the user.
def add_to_watchlist(user_data, movie):

    watchlist = []

    user_data = {"watchlist": watchlist}

    for value in user_data.values():
        watchlist.append(movie)

    return user_data


# watch_movie function takes in two parameters (user_data, title) and once the user watches a movie included in the user's watchlist,/ 
# the function will remove the movie from the user's watchlist and add it to the user's watched list.
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


# get_watched_avg_rating function calculates the average rating of all movies in the user's watched list.
def get_watched_avg_rating(user_data):

    ratings_list = []

    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    
    if ratings_list == []:
        return 0
    else: 
        return sum(ratings_list) / len(ratings_list)


# get_most_watched_genre function determines which genre is most frequently occuring in the watched list.
def get_most_watched_genre(user_data):

    genre_list = []

    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    if genre_list == []:
        return None
    
    # Counter function is imported from the Collections library which creates a dictionary of genres where the value of each genre key /
    # is the frequency of those genres in the user's watched list. The Counter is then used to return a list of the most common genre / 
    # and the number of times it appeard in the user's watched list. 
    else:
        genre_frequency = Counter(genre_list)
        most_common_genre_frequency = genre_frequency.most_common(1)
        most_common_genre = most_common_genre_frequency[0][0]
        return most_common_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# get_unique_watched function identifies which movies the user has watched that none of their friends have watched.
def get_unique_watched(user_data):

    # an empty set is created to store the user and friend's watched movies, respectively.
    user_compiled_watched_set = set()
    friends_unique_compiled_set = set()

    # each movie dictionary in the user and user's friends watched lists are converted into a tuple where each key-value dictionary pair/ 
    # is stored as a set within the tuple. Each tuple is then appended to the the respective set.
    for movie in user_data["watched"]:
        user_compiled_watched_set.add(tuple(movie.items()))

    for i in range(len(user_data["friends"])):
            for watched in user_data["friends"][i].values():
                for movie in watched:
                    friends_unique_compiled_set.add(tuple(movie.items()))

    # Once the movies watched by the user and user's friends are in sets, duplicate values are removed, and we are able to use the /
    # .difference() function to evaluate what movies the user has watched that none of their friends have.
    user_but_not_friends = user_compiled_watched_set.difference(friends_unique_compiled_set)

    movie_user_has_watched_but_friends_have_not = []

    # each tuple in the respective set is converted back into a dictionary. These movie dictionaries are then appended to a list.
    for tup in user_but_not_friends:
        user_but_not_friends_dict_type = dict(tup)
        movie_user_has_watched_but_friends_have_not.append(user_but_not_friends_dict_type)
        
    return movie_user_has_watched_but_friends_have_not

# get_friends_unique_watched function identifies which movies the user's friends have watched that the user has not watched.
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

    movie_friends_have_watched_but_user_has_not = []

    for tup in friends_but_not_user:
        friends_but_not_user_dict_type = dict(tup)
        movie_friends_have_watched_but_user_has_not.append(friends_but_not_user_dict_type)
        
    return movie_friends_have_watched_but_user_has_not


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


# get_available_recs function creates a list of movie recommendations based on movies watched by the user's friends and not yet watched /
# by the user if the user subscribes to the app that hosts the movie.
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


# get_new_rec_by_genre function creates a list of movie recommendations based on movies watched by the user's friends and not yet watched /
# by the user if the movie's genre is the same as the user's most frequently watched genre.
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


# get_rec_from_favorites function creates a list of movie recommendations based on movies that the user has watched that none of their /
# friends have watched if the user has included the movie in their favorites list.
def get_rec_from_favorites(user_data):

    user_watched_movie = get_unique_watched(user_data)

    user_watched_movie_set = set()
    user_favorite_movie_set = set()

    for movie in user_watched_movie:
        user_watched_movie_set.add(tuple(movie.items()))

    for movie in user_data["favorites"]:
        user_favorite_movie_set.add(tuple(movie.items()))

    # Once the movies watched by only the user and the user's favorite movies are in sets, duplicate values are removed and we are able /
    # to use the .intersection() function to evaluate what movies are in both sets.
    user_watched_favorites = user_favorite_movie_set.intersection(user_watched_movie_set)

    recommended_movie_list_from_favorites = []

    for tup in user_watched_favorites:
        user_watched_favorites_dict_type = dict(tup)
        recommended_movie_list_from_favorites.append(user_watched_favorites_dict_type)
        
    return recommended_movie_list_from_favorites
