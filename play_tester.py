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

# movie = {
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }

# user_data = {
#     "watched": []
# }


# list_data = []

# list_data.append(user_data)
# print(list_data)

# print(list_data[0])
# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

# print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())

# # Wave 05 user data
# print("\n-----Wave 05 user_data-----")
# pp.pprint(clean_wave_5_data())

# watched_by_genre = {"fantasy": 1}

# if "sci-fi" in watched_by_genre.keys():
#     watched_by_genre["sci-fi"] += 1
# else:
#     watched_by_genre["sci-fi"] = 1

# print(watched_by_genre)

user_data = clean_wave_5_data()

# print(clean_data["friends"])

# print(clean_data["friends"][0]["watched"][0]["title"])

# print(clean_data)

# friends_watched_movies = set()

# user_watched_movies = set()

# for friend in clean_data["friends"]:
#     for watched_list in friend["watched"]:
#         friends_watched_movies.add(watched_list['title'])

# # print(friends_watched_movies)

# for movie in clean_data["watched"]:
#     user_watched_movies.add(movie["title"])

# # print(friends_watched_movies)

# unique_movie_titles = (user_watched_movies - friends_watched_movies)

# unique_movies_data = []

# for movie in unique_movie_titles:
#     for i in range(len(clean_data["watched"])):
#         if movie == clean_data["watched"][i]["title"]:
#             unique_movies_data.append(clean_data["watched"][i])

# print(unique_movies_data)


# friends_watched_movies = set()
# user_watched_movies = set()

# for friend in user_data["friends"]:
#     for watched_list in friend["watched"]:
#         friends_watched_movies.add(watched_list['title'])

# for movie in user_data["watched"]:
#     user_watched_movies.add(movie["title"])

# unique_movie_titles = (friends_watched_movies - user_watched_movies)

# print(unique_movie_titles)

# unique_movies_data = []

# # for movie in unique_movie_titles:
# #     for i in range(len(user_data["friends"])):
# #         print(i)
# #         for n in range (len(user_data["friends"][i])):
# #             print(n)
#             # if movie == user_data["friends"][i]["watched"][n]["title"]:
#                 # unique_movies_data.append(user_data["friends"][i]["watched"])

# for movie in unique_movie_titles:
#     for friend in (user_data["friends"]):
#         print(friend)
#         for i in range(len(friend["watched"])):
#             # print(friend['watched'][i])
#             if movie == friend["watched"][i]["title"]:
#                 unique_movies_data.append(friend["watched"][i])
# #         for n in range (len(user_data["friends"][i])):
# #             print(n)
# print("-----------------------------")
# print(unique_movies_data)

# available_recs = []

# user_subscriptions = user_data["subscriptions"]

# for friends_list in user_data["friends"]:
#     for movie in friends_list["watched"]:
#         if movie["host"] in user_subscriptions and movie not in user_data["watched"]:
#             available_recs.append(movie)

# print(available_recs)

# iterate through 

# print(get_most_watched_genre(user_data))

# recs = []
# favorite_genre = get_most_watched_genre(user_data)
# all_recs = get_available_recs(user_data)

# for rec in all_recs:
#     if rec["genre"] == favorite_genre:
#         recs.append(rec)

# print(recs)

# recs = []

# unique_watched = get_unique_watched(user_data)

# for movie in unique_watched:
#     if movie in user_data["favorites"]:
#         recs.append(movie)

# return recs

# friends_watched_movies = set()


# user_subscriptions = user_data["subscriptions"]

# for friends_list in user_data["friends"]:
#     for movie in friends_list["watched"]:
#         if movie["host"] in user_subscriptions and movie not in user_data["watched"]:
#             recs.append(movie)

