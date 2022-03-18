# ------------- WAVE 1 --------------------
#this is where I will create a function
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    movie_dictionary ={}
    movie_dictionary["title"] = title
    movie_dictionary["genre"] = genre
    movie_dictionary["rating"] = rating

    return movie_dictionary

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
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

