# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

movie_title = "Title A"
genre = "Horror"
rating = 8

user_data = {
        "watched": []
    }

def create_movie(title, genre, rating):
    
    if title and genre and rating:
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

new_dict = create_movie(movie_title, genre, rating)
# print(new_dict)
# print(add_to_watched(user_data, new_dict))


janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }
def watch_movie(user_data, movie_title):

    for index in range(0, len(user_data["watchlist"])):
        nested_movie_title_watched = user_data["watchlist"][index]["title"]
        if movie_title in nested_movie_title_watched:
            correct_movie = user_data["watchlist"][index]
            user_data["watched"].append(correct_movie)
        user_data["watchlist"].remove(correct_movie)
        
    print(user_data["watchlist"])
    print(user_data["watched"])
    return user_data


test = watch_movie(janes_data, MOVIE_TITLE_1)
# print(test)


# print(test)
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
