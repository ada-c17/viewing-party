# # ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating

    return movie_dict

def add_to_watched(user_data, movie):
    new_movie = create_movie(movie["title"],movie["genre"],movie["rating"])
    user_data["watched"] = [new_movie]

    return user_data

def add_to_watchlist(user_data, movie):
    new_movie = create_movie(movie["title"],movie["genre"],movie["rating"])
    user_data["watchlist"] = [new_movie]

    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:      
            movie = user_data["watchlist"][i]
            user_data["watched"].append(movie)
            del user_data["watchlist"][i]

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

