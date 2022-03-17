# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #if title == True and genre == True and rating == True:
    #if isinstance(title, str) and isinstance(genre, str) and isinstance(rating, str):   
    if title != None and genre != None and rating != None:
        movie_dict = {"title":title, "genre":genre, "rating":rating}
        return movie_dict
    else: 
        return None




def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data    

#hi
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

