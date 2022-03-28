# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

# print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())
# user_data= clean_wave_3_data()
# friends_movie_data = user_data["friends"]






user_data = {
    "watchlist": [
        FANTASY_1,
        movie_to_watch
    ],
    "watched": [FANTASY_2]
}



def watch_movie(user_data, MOVIE_TITLE_1):

    watched_movie = []
    if movie_t0_watch
    
    for i in range(len("watchlist")): 
        if MOVIE_TITLE_1 == user_data["watchlist"][i]["title"]:
            watched_movie.append(user_data["watchlist"][i])
            user_data["watched"]= watched_movie
            del user_data["watchlist"][0]
            return user_data

    else:
        return user_data

print("watched")
watch_movie(user_data, MOVIE_TITLE_1)

# new_list= []
# recommendations_list = []
# for friend in USER_DATA_5["friends"]:
#     for movie in friend["watched"]:
#         if movie not in USER_DATA_5["watched"]:
#             new_list.append(movie)
#     for movie in new_list:
#         if movie["genre"]== "Fantasy":
#             recommendations_list.append(movie)

#     print (f"This is new list: {new_list}")
#     print (f"This is rec lis : {recommendations_list}")

# pp.pprint(USER_DATA_5["friends"][1])

# user_watched= [FANTASY_1,
#                 FANTASY_2,
#                 FANTASY_3,
#                 ACTION_1,
#                 INTRIGUE_1,
#                 INTRIGUE_2,
# ]
# friends_movie_data = user_data["friends"]  
# first_friend_watched_data = [
#                 FANTASY_1,
#                 FANTASY_3,
#                 FANTASY_4,
#                 HORROR_1,
#             ]
# second_friend_watched_data = [ FANTASY_1,
#                 ACTION_1,
#                 INTRIGUE_1,
#                 INTRIGUE_3,
#                 ]
# pp.pprint(USER_DATA_5)
# pp.pprint(f"this is user_data/friends[0]: {first_friend_watched_data}")
# pp.pprint(f"this is user_data/friends[1]: {second_friend_watched_data}")
# pp.pprint(f"this is the 1st comparison list: {comparison_1}")
# friends_unique_movies = []
# comparison_1 =[]
# comparison_2 =[]
# for movie in first_friend_watched_data:
#     if movie not in user_watched:
#        friends_unique_movies.append(movie)   
# for movie in second_friend_watched_data:
#     if movie not in user_watched:
#        friends_unique_movies.append(movie)
# pp.pprint(f"this is the 1st comparison list: {comparison_1}")
# pp.pprint(f"this is the 1st comparison list: {comparison_1}")   
# pp.pprint(f"this is the 2nd comparison list: {comparison_2}")  
# pp.pprint(f"this is the unique list: {friends_unique_movies}")  
# for movie in user_watched:
#     if movie  not in second_friend_watched_data:
#         comparison_2.append(movie)
# for movie in comparison_2:
#     if movie in comparison_1 and comparison_2:
#         unique_list.append(movie)
#     print(unique_list)


# pp.pprint(f"this is the 1st comparison list: {comparison_1}")   
# pp.pprint(f"this is the 2nd comparison list: {comparison_2}") 
# pp.pprint(f"this is the unique list: {unique_list}") 
# pp.pprint(f"this is the usesr data 3list: {unique_list}") 

# pp.pprint(clean_wave_3_data())
# print(movie)
# # print()
# print(unique_list)

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())
# pp.pprint(copy.deepcopy(USER_DATA_4))
# pp.pprint(copy.deepcopy(HORROR_1b))
# pp.pprint(copy.deepcopy(FANTASY_4))
# pp.print( copy.deepcopy(HORROR_1b))



# user_watched = []
# friends_watched = []
# comparison_list =[]
# user_data = USER_DATA_4
# reccomendations= []
# def get_rec_movie(user_data):
#     for i in range(len(user_data)):
#         # user_watched = user_data["watched"][i]
#         user_watched.append(user_data["watched"][i])
#     for i in range(len(user_data["friends"])):
#         for j in range(len(user_data["friends"][i]["watched"])):
#             friends_watched.append(user_data["friends"][i]["watched"][j])
#         # user_watched.append(user_data["watched"][i])
#     for movie in friends_watched:
#         if movie not in user_watched:
#             comparison_list.append(movie)
#     for movie in comparison_list:
#         if movie["host"] in user_data["subscriptions"]:
#             print("The host  matches")
#             reccomendations.append(movie)

# def get_available_recs(user_data):

#     for i in range(len(user_data)):
#         # user_watched = user_data["watched"][i]
#         user_watched.append(user_data["watched"][i])
#     for i in range(len(user_data["friends"])):
#         for j in range(len(user_data["friends"][i]["watched"])):
#             friends_watched.append(user_data["friends"][i]["watched"][j])
#         # user_watched.append(user_data["watched"][i])
#     for movie in friends_watched:
#         if movie not in user_watched:
#             comparison_list.append(movie)
#     for movie in comparison_list:
#         if movie["host"] in user_data["subscriptions"]:
#             recommendations.append(movie)
#     # print(f"friends watched: {friends_watched}")
#     return recommendations     
#     # pp.pprint(clean_wave_4_data())

# get_available_recs(user_data)
# pp.pprint(f"This is user_watched {user_watched}")
# pp.pprint(f"This is friends_watched {friends_watched}")
    # pp.pprint(comparison_list[0]["host"])
    # pp.pprint(user_data["friends"][0])
    # pp.pprint(reccomendations)
    # pp.pprint(f"friends data: {friends_watched}")
    # pp.pprint(user_data["subscriptions"])        
    # print(f"This is the {comparison_list}")
    # print(user_data["subscriptions"])
    # print(user_data)
    # print(user_data["friends"][0]["watched"])
    

# get_rec_movie(user_data)





# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
