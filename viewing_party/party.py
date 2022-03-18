# ------------- WAVE 1 --------------------
'''
###
TWO or just one??
The next two tests are about the add_to_watched() function.
###

There are three tests about a watch_movie() function.
In party.py, there should be a function named watch_movie. This function should...

take two parameters: user_data, title
the value of user_data will be a dictionary with a "watchlist" and a "watched"
This represents that the user has a watchlist and a list of watched movies
the value of title will be a string
This represents the title of the movie the user has watched
If the title is in a movie in the user's watchlist:
remove that movie from the watchlist
add that movie to watched
return the user_data
If the title is not a movie in the user's watchlist:
return the user_data
Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.
'''

def create_movie(title, genre, rating):
    if title and genre and rating:
        print("hello")
        dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return dict

    return None

def add_to_watched(user_data, movie):
    user_data_copy = user_data.copy()

    # if movie:
    user_data_copy["watched"].append(movie)

    return user_data_copy

def add_to_watchlist(user_data, movie):
    user_data_copy = user_data.copy()

    user_data_copy["watchlist"].append(movie)

    return user_data_copy

def watch_movie(user_data, title):
    # user_data_copy = user_data.copy()
    for movie_entry in user_data["watchlist"]:
        if movie_entry["title"] == title:
            user_data["watched"].append(movie_entry)
            user_data["watchlist"].remove(movie_entry)

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

