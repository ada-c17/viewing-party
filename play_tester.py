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

def add_to_watched(user_data, movie):

    #put movie inside value list of of movies
    for key in user_data:
        user_data[key].append(movie)

    print(user_data)
    #return user data

    return user_data
movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
user_data = {
        "watchlist": []
    }

    # Act
updated_data = add_to_watchlist(user_data, movie)
print(updated_data)

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
