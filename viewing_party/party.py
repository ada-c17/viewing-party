# ------------- WAVE 1 --------------------

from curses import keyname
from xml.sax.handler import EntityResolver

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1, USER_DATA_2


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else: 
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
    }

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------