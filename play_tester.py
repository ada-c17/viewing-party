# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
print("\n-----Wave 01 test data-----")
pp.pprint(HORROR_1)
pp.pprint(FANTASY_1)
pp.pprint(FANTASY_2)

print("\n-----Wave 02 user_data-----")
pp.pprint(clean_wave_2_data())

def get_most_watched_genre(user_data):
    fantacy_count = 0
    action_count = 0
    intrigue_count = 0
    
    if len(user_data["watched"]) < 1:
        most_watched_genre = None 
        return most_watched_genre

    for movie in user_data["watched"]:
        if movie["genre"] == "Fantacy":
            fantacy_count += 1
        if movie["genre"] == "Action":
            action_count += 1
        if movie["genre"] == "Intrigue":
            intrigue_count += 1

    if fantacy_count > action_count and fantacy_count > intrigue_count:
        most_watched_genre = "Fantacy"
    if action_count > fantacy_count and action_count > intrigue_count:
        most_watched_genre = "Action"
    if intrigue_count > action_count and intrigue_count > fantacy_count:
        most_watched_genre = "Intrigue"
    return most_watched_genre


print("\n-----Wave 03 user_data-----")
pp.pprint(clean_wave_3_data())

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
            for title in movie["title"]:
                if title == unique_movie:
                    user_unique_watched_list.append(user_data["watched"][movie])

    return user_unique_watched_list

# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
