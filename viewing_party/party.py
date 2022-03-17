# ------------- WAVE 1 --------------------

from hashlib import new


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
    updated_list = []
    for film in user_data["watched"]:
        updated_list.append(film)
    updated_list.append(movie)
    user_data["watched"] = updated_list    
    return user_data

def add_to_watchlist(user_data, movie):
    updated_list = []
    for film in user_data["watchlist"]:
        updated_list.append(film)
    updated_list.append(movie)
    user_data["watchlist"] = updated_list    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#def get_watched_avg_rating(user_data):
#    if len(user_data["watched"]) == 0:
#        average = 0.0
#        return average
    


#    return average

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

