import copy


# from typing import final
# from testing_values import *

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title is None or genre is None or rating is None:
        return None
    movie_dict["title"] = title
    movie_dict["genre"] =  genre 
    movie_dict["rating"] =  rating
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"] =  [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] =  [movie]
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        print(f"i:{i}")
        print(f"value:{user_data['watchlist'][i]['title']}")
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    else:
        avg_list = []
        for i in range(len(user_data["watched"])):
            avg_list.append(user_data["watched"][i]["rating"])
        return sum(avg_list) / len(avg_list)


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    else:
        most_watched_dict = {}
        for i in range(len(user_data["watched"])):
            genre = user_data["watched"][i]["genre"]
            if genre in most_watched_dict:
                most_watched_dict[genre] += 1
            else:
                most_watched_dict[genre] = 1
        return max(most_watched_dict, key=most_watched_dict.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = copy.deepcopy(user_data['watched'])
    friends_watched_list = []
    final_list = []


    for j in range(len(user_data['friends'])):
        for k in range(len(user_data['friends'][j]['watched'])):
            friends_watched_list.append(user_data['friends'][j]['watched'][k]['title'])
            

    final_list = [unique_movies[i] for i in range(len(unique_movies)) \
        if not unique_movies[i]['title'] in friends_watched_list]
            
    return final_list

def get_friends_unique_watched(user_data):
    unique_movies = copy.deepcopy(user_data['friends'])

    users_watched_list = []
    final_list = []

    for i in range(len(user_data['watched'])):
        users_watched_list.append(user_data['watched'][i]['title'])
    # print(users_watched_list)
    for j in range(len(unique_movies)):
        # CODE FOR LIST COMPREHENSION BUT FOR SOME REASON DOES NOT WORK LOL
        # final_list = [unique_movies[j]['watched'][k] for k in range(len(unique_movies[j]['watched'])) \
        #     if not unique_movies[j]['watched'][k]['title'] in users_watched_list]
        for k in range(len(unique_movies[j]['watched'])):
            #BUT THIS METHOD WORKS
            if not unique_movies[j]['watched'][k]['title'] in users_watched_list:
                if not unique_movies[j]['watched'][k] in final_list:
                    final_list.append(unique_movies[j]['watched'][k])

    return final_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_subscriptions = user_data['subscriptions']
    unique_movies = copy.deepcopy(user_data['friends'])
    users_watched_list = []
    final_list = []

    for i in range(len(user_data['watched'])):
        users_watched_list.append(user_data['watched'][i]['title'])

    for j in range(len(unique_movies)):
        for k in range(len(unique_movies[j]['watched'])):
            if not unique_movies[j]['watched'][k]['title'] in users_watched_list and unique_movies[j]['watched'][k]['host'] in available_subscriptions:
                if not unique_movies[j]['watched'][k] in final_list:
                    final_list.append(unique_movies[j]['watched'][k])

    return final_list


    




# janes_data = {
#     "watched": [{
#         "title": "a",
#         "genre": "b",
#         "rating": "c"
#     }, 
#     {
#         "title": "d",
#         "genre": "e",
#         "rating": "f"
#     }],
#     "friends" : [
#         {"watched": [{
#                 "title": "a",
#                 "genre": "b",
#                 "rating": "c"
#         },
#         {
#                 "title": "cc",
#                 "genre": "dd",
#                 "rating": "ee"
#         }]
#         },
#         {"watched": [{
#                 "title": "dd",
#                 "genre": "ee",
#                 "rating": "ff"
#         },
#         {
#                 "title": "gg",
#                 "genre": "hh",
#                 "rating": "ii"
#         }]
#         }
#     ]  
 
# }

# get_unique_watched(USER_DATA_3)






        


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

