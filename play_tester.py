# import source code
from lib2to3.pgen2.pgen import generate_grammar
from multiprocessing.sharedctypes import Value
from operator import index
from os import remove
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

#----------WAVE01-------------

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

# print("\n-----Wave 03 user_data-----")
# # pp.pprint(clean_wave_3_data())
def get_unique_watched(user_data):
    user_movies = []
    friend_movies = []
    user_unique_movies = []
    for selection in user_data['friends']:
        for movie in selection['watched']:
            friend_movies.append(movie)
    for movie in user_data['watched']:
            user_movies.append(movie)
    for movie in user_movies:
        if movie not in friend_movies:
            user_unique_movies.append(movie)
    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_movies = []
    friend_movies = []
    friend_undup_movies = []
    friend_unique_movies = []
    for movie in user_data['friends']:
        for title in movie['watched']:
            friend_movies.append(title)
    for movie in user_data['watched']:
            user_movies.append(movie)
    for movie in friend_movies:
        if movie not in friend_undup_movies:
            friend_undup_movies.append(movie)
    for movie in friend_undup_movies:
        if movie not in user_movies:
            friend_unique_movies.append(movie)
    return friend_unique_movies



# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# # Wave 05 user data
# print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())