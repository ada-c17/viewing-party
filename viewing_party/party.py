#----------WAVE01-------------
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5
# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        movie = None
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    movie = user_data["watchlist"][0]
    user_data["watched"].append(movie)
    user_data["watchlist"].remove(movie)
    return user_data

janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }

movie = create_movie(MOVIE_TITLE_1, GENRE_1, RATING_1)

updated_data = add_to_watched(janes_data, movie)

updated_data = watch_movie(janes_data, MOVIE_TITLE_1)
# def test_moves_movie_from_watchlist_to_empty_watched():
#     # Arrange
#     janes_data = {
#         "watchlist": [{
#             "title": MOVIE_TITLE_1,
#             "genre": GENRE_1,
#             "rating": RATING_1
#         }],
#         "watched": []
#     }

#     # Act
#     updated_data = watch_movie(janes_data, MOVIE_TITLE_1)

#     # Assert
#     assert len(updated_data["watchlist"]) is 0
#     assert len(updated_data["watched"]) is 1
# 
# # *******************************************************************************************
# ****** Add assertions here to test that the correct movie was added to "watched" **********
# *******************************************************************************************


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

