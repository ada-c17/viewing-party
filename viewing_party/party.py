# ------------- WAVE 1 --------------------

from audioop import avg
from collections import Counter
from shutil import move


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

    for value in user_data:
        watched.append(movie)
                
    return user_data

def add_to_watchlist(user_data, movie):

    watchlist = []

    user_data = {"watchlist": watchlist}

    for value in user_data:
        watchlist.append(movie)

    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]
    watched = user_data["watched"]

    watchlist_index = len([ele for ele in watchlist if isinstance(ele, dict)])

    for i in range(watchlist_index):
        if (watchlist[i]["title"]) == title:
            watched_movie = watchlist.pop(i)

            for value in user_data:
                watched.append(watched_movie)
                return user_data

        elif (watchlist[i]["title"]) != title:
            print("test") # delete print statement but get check for errors before and after

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    ratings_list = []
    #watched = user_data["watched"] - delete if no errors

    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    
    if ratings_list == []:
        return 0
    else: 
        return sum(ratings_list) / len(ratings_list)

def get_most_watched_genre(user_data):

    genre_list = []
    genre_count = {}

    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    if genre_list == []:
        return None
    
    else:
        genre_frequency = Counter(genre_list)
        most_common_genre_frequency = genre_frequency.most_common(1)
        most_common_genre = most_common_genre_frequency[0]
        return most_common_genre[0]
        
        
        # for genre in genre_list:
        #     print(genre_list)
        #     if genre not in genre_count:
        #         genre_count[genre] = 1
        #     else:
        #         genre_count[genre] += 1
        #         print(genre_list)
        #         print(genre_count)
        #         genre_count_set = set(genre_count)
        #         print()
        #         print(genre_count_set)
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_compiled_watched_set = set()
    friends_unique_compiled_set = set()

    for movies in user_data["watched"]:
        user_compiled_watched_set.add(tuple(movies.items()))

    for i in range(len(user_data["friends"])):
            for friend, movies in user_data["friends"][i].items():
                for watched in movies:
                    friends_unique_compiled_set.add(tuple(watched.items()))

    user_but_not_friends = user_compiled_watched_set.difference(friends_unique_compiled_set)

    movies_user_has_watched_but_friends_have_not = []

    for tup in user_but_not_friends:
        user_but_not_friends_dict_type = dict(tup)
        movies_user_has_watched_but_friends_have_not.append(user_but_not_friends_dict_type)
        
    return movies_user_has_watched_but_friends_have_not


def get_friends_unique_watched(user_data):

    user_compiled_watched_set = set()
    friends_unique_compiled_set = set()

    for movies in user_data["watched"]:
        user_compiled_watched_set.add(tuple(movies.items()))

    for i in range(len(user_data["friends"])):
            for friend, movies in user_data["friends"][i].items():
                for watched in movies:
                    friends_unique_compiled_set.add(tuple(watched.items()))

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

    recommended_movies_list = []

    user_subscriptions = user_data["subscriptions"]

    for movie in movie_recommended_by_friends:
        for key, value in movie.items():
            if key == "host":
                if value in user_subscriptions:
                    recommended_movies_list.append(movie)

    return(recommended_movies_list)





# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

