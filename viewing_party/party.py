# ------------- WAVE 1 --------------------

from sys import argv


def create_movie(movie_title, genre, rating):
    dict = {}

    if movie_title == None or genre == None or rating == None:
        return None 
    else:
        dict["title"] = movie_title
        dict["genre"] = genre
        dict["rating"] = rating

    return dict 


def add_to_watched(user_data, create_movie):
    user_data = {}
    list = []
    user_data["watched"] = list
    list.append(create_movie)

    # if user_data == None:
    #     return dict["watched"] == [] 
    # else:
    #     dict["watched"] = list_movie

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

