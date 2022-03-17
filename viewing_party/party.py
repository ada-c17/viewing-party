# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie_dict = {}
    new_movie_dict["title"] = title
    new_movie_dict["genre"] = genre
    new_movie_dict["rating"] = rating
    for value in new_movie_dict.values():
        if value == None:
            return None
    return new_movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 -------∫-------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
