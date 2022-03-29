# ------------- WAVE 1 --------------------


from logging.handlers import WatchedFileHandler
from tkinter import W


def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie = {
            "title": title, 
            "genre": genre,
            "rating": rating}
        return new_movie
    else:
        new_movie = None
        return new_movie

# am i supposed to make this or is the test making it?
# user_data = {
#         "watched": [
#             {
#                 "title": "Title A",
#                 "genre": "Horror",
#                 "rating": 3.5

#             }
            
#         ]
#     }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie) 
            user_data["watched"].append(movie)
            return user_data

    return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_ratings = 0
    num_of_movies = len(user_data["watched"])
    
    if len(user_data["watched"]) < 1:
        watched_avg_rating = 0.0 
        return watched_avg_rating

    for movie in user_data["watched"]:
        total_ratings += movie["rating"]

    watched_avg_rating = total_ratings / num_of_movies

    return watched_avg_rating

def get_most_watched_genre(user_data):
    fantasy_count = 0
    action_count = 0
    intrigue_count = 0
    
    if len(user_data["watched"]) < 1:
        most_watched_genre = None 
        return most_watched_genre

    for movie in user_data["watched"]:
        if movie["genre"] == "Fantasy":
            fantasy_count += 1
        if movie["genre"] == "Action":
            action_count += 1
        if movie["genre"] == "Intrigue":
            intrigue_count += 1

    if fantasy_count > action_count and fantasy_count > intrigue_count:
        most_watched_genre = "Fantasy"
    if action_count > fantasy_count and action_count > intrigue_count:
        most_watched_genre = "Action"
    if intrigue_count > action_count and intrigue_count > fantasy_count:
        most_watched_genre = "Intrigue"
    return most_watched_genre




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.append(movie["title"])
    
    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    user_unique_watched_set = user_watched_set.difference(friend_watched_set)
    user_unique_watched_list = []

    for unique_movie in user_unique_watched_set:
        for movie in user_data["watched"]:
            if movie["title"] == unique_movie:
                user_unique_watched_list.append(movie)

    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.append(movie["title"])
    
    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    friend_unique_watched_set = friend_watched_set.difference(user_watched_set)
    friend_unique_watched_list = []

    for unique_movie in friend_unique_watched_set:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie not in friend_unique_watched_list:
                    if movie["title"] == unique_movie:
                        friend_unique_watched_list.append(movie)

    return friend_unique_watched_list


##I know if i reverse this somehow it would work more eloquently but i couldnt seem to make that work


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_watched_movie_title_list = []
    user_watched_movie_title_list = []
    
    for movie in user_data["friends"]["watched"]:
        friend_watched_movie_title_list.append("title")
    for movie in user_data["watched"]:
        user_watched_movie_title_list.append("title")

    friend_watched_movie_title_set = set(friend_watched_movie_title_list)
    user_watched_movie_title_set = set(user_watched_movie_title_list)
    friend_recommends_title_set = friend_watched_movie_title_set.difference(user_watched_movie_title_set)
    friend_recommends_movie_list=[]

    for recommended_movie in friend_recommends_title_set:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie not in friend_recommends_movie_list:
                    if movie["title"] == recommended_movie:
                        friend_recommends_movie_list.append(movie)
    
    friend_recommended_movie_host = []
    user_subscriptions = []

    for subscription in user_data["subscriptions"]:
        user_subscriptions.append(subscription)
    for title in friend_recommends_title_set:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie["host"] not in friend_recommended_movie_host:
                    friend_recommended_movie_host.append("host")
    
    friend_recommended_movie_host_set = set(friend_recommended_movie_host)
    user_subscriptions_set = set(user_subscriptions)

    host_subscription_match = friend_recommended_movie_host_set.intersection(user_subscriptions_set)
    avalible_recommended_movies_list = []

    for match in host_subscription_match:
        for movie in friend_recommends_movie_list:
            if movie["host"] == match:
                if movie not in avalible_recommended_movies_list:
                    avalible_recommended_movies_list.append(movie)

    return avalible_recommended_movies_list


# -----------------------------------------
# ----------ALT WAVE 4 --------------------
# -----------------------------------------

# def get_available_recs(user_data):
#     friend_watched_movie_title_list = []
#     user_watched_movie_title_list = []
    
#     for movie in user_data["friends"]["watched"]:
#         friend_watched_movie_title_list.append(movie["title"])
#     for movie in user_data["watched"]:
#         user_watched_movie_title_list.append(movie["title"])

#     friend_watched_movie_title_set = set(friend_watched_movie_title_list)
#     user_watched_movie_title_set = set(user_watched_movie_title_list)
#     friend_recommends_title_set = friend_watched_movie_title_set.difference(user_watched_movie_title_set)
#     friend_recommends_movie_list=[]

#     for recommended_movie in friend_recommends_title_set:
#         for friend in user_data["friends"]:
#             for movie in friend["watched"]:
#                 if movie not in friend_recommends_movie_list:
#                     if movie["title"] == recommended_movie:
#                         friend_recommends_movie_list.append(movie)
    
#     friend_recommended_movie_host = []
#     user_subscriptions = []

#     for subscription in user_data["subscriptions"]:
#         user_subscriptions.append(subscription)
#     for title in friend_recommends_title_set:
#         for friend in user_data["friends"]:
#             for movie in friend["watched"]:
#                 if movie["host"] not in friend_recommended_movie_host:
#                     friend_recommended_movie_host.append(movie["host"])
    
#     friend_recommended_movie_host_set = set(friend_recommended_movie_host)
#     user_subscriptions_set = set(user_subscriptions)

#     host_subscription_match = friend_recommended_movie_host_set.intersection(user_subscriptions_set)
#     avalible_recommended_movies_list = []

#     for match in host_subscription_match:
#         for movie in friend_recommends_movie_list:
#             if movie["host"] == match:
#                 if movie not in avalible_recommended_movies_list:
#                     avalible_recommended_movies_list.append(movie)

#     return avalible_recommended_movies_list



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# im willing to continue working on this 
# but im worried about getting further behind
# so im going to submit it now, incomplete
#with plans to circle back this weekend










