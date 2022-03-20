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

# print("wave 1 test 8 playtest below")

# movie_to_watch = HORROR_1
# janes_data = {
#     "watchlist": [
#         FANTASY_1,
#         movie_to_watch
#     ],
#     "watched": [FANTASY_2]
# }
# updated_data = watch_movie(janes_data, movie_to_watch["title"])

# print(f"movie to watch: {movie_to_watch}")
# print(updated_data)
# print(len(updated_data["watchlist"]))# == 1
# print(len(updated_data["watched"])) # == 2
# print(updated_data["watched"][0]["title"]) # == FANTASY_2["title"]
# print(updated_data["watchlist"][0]["rating"]) # == FANTASY_1["rating"]


# print("\n-----Wave 02 user_data-----")
pp.pprint(clean_wave_2_data())

print("~~~")
janes_data = clean_wave_2_data()
# janes_data = {
#         "watched": []
#     }

# def get_watched_avg_rating(user_data):
#     num_movies_watched = 0
#     rating_sum = 0

#     for lst_name, lst_contents in user_data.items():
#         num_movies_watched += len(lst_contents)
        
#         for movie in lst_contents:
#             rating_sum += movie["rating"]
        
#         if num_movies_watched == 0:
#             average_rating = 0
#         else:
#             average_rating = rating_sum/num_movies_watched

#     return average_rating

# print(get_watched_avg_rating(janes_data))

print("test 12:")

# def get_most_watched_genre(user_data):

    # initialize empty dictionary
    # if genre type is not a key in the dictonary, create key
    # with default value of 1
    # for movie in watched list,
    # update value count 

    # user_genre_count = {}

    # for movie in janes_data["watched"]:
    #     genre = movie["genre"]
    #     print(genre)
    #     if genre not in user_genre_count.keys():
    #         user_genre_count[genre] = 1
    #     else:
    #         user_genre_count[genre] += 1
    #     print(user_genre_count)

    # most_watched = max(user_genre_count, key=user_genre_count.get)
    
    # return most_watched

print(get_most_watched_genre(janes_data))
# print(janes_data["watched"][0]["genre"])





#print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())

# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
