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

#print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())

# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())


# janes_data = {
#     "watchlist": [{
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }],
#     "watched": []
# }
    
# print(f'{janes_data["watchlist"]=}')

amandas_data = clean_wave_3_data()

def get_friends_unique_watched(user_dict):
    friends_watched_list = user_dict["friends"]
    combined_friends_list = []
    for watched_dict in friends_watched_list:
        combined_friends_list.extend(watched_dict["watched"])
    users_watched_list = user_dict["watched"]
    unique_watched = []
    for movie in combined_friends_list:
        if movie not in users_watched_list:
            unique_watched.append(movie)
    print(f"{combined_friends_list=}")
    print(f"{users_watched_list=}")
    print("this is the list: \n")
    return unique_watched


print(get_friends_unique_watched(amandas_data))
# # pp.pprint(amandas_data)