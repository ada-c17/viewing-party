# ------------- WAVE 1 --------------------

# this is a test change

def create_movie(title, genre, rating):
    if (title == None) or (genre == None) or (rating == None):
       return None
    else:
        created_movie_dict = {}
        created_movie_dict["title"] = title
        created_movie_dict["genre"] = genre
        created_movie_dict["rating"] = rating
        return created_movie_dict
    
    
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    user_data["watchlist"][0]["title"] = movie["title"]
    return user_data

# In `party.py`, there should be a function named `watch_movie`. This function should...

# - take two parameters: `user_data`, `title`
#   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
#     - This represents that the user has a watchlist and a list of watched movies
#   - the value of `title` will be a string
#     - This represents the title of the movie the user has watched
# - If the title is in a movie in the user's watchlist:
#   - remove that movie from the watchlist
#   - add that movie to watched
#   - return the `user_data`
# - If the title is not a movie in the user's watchlist:
#   - return the `user_data`

def watch_movie(user_data, title):
    if user_data["watchlist"][0]["title"] == title:
        user_data["watchlist"].remove(user_data["watchlist"][0])
        user_data["watched"].append(title)
        return user_data
    else:
        return user_data

# def watch_movie(user_data, title):
#     if user_data["watchlist"][0]["title"] == title:
#         specific_title = user_data["watchlist"][0]["title"]
#         user_data["watchlist"].remove(specific_title)
#         user_data["watched"].append(user_data["watchlist"])
#     else:
#         return user_data


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

