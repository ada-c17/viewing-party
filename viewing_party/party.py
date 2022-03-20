# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Input: title (string), genre (string), rating (float)
    Output: If parameters are truthy, return dictionary. If not, return None
    """
    movies = {}

    if (title and genre and rating):
        movies["title"] = title
        movies["genre"] = genre
        movies["rating"] = rating
        return movies
    
    return None


def add_to_watched(user_data, movie):
    """
    Input: user_data (dictionary with key = "watched" and value = list of dictionaries), movie (dictionary from create_movie)
    Output: return user_data
    """
    # Add movie (dictionary) to the "watched" list (list of dictionaries)

    # What's passed in:
        # user_data = { "watched": []}

        # movie = {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}
    
    if "watched" in user_data:
        user_data["watched"].append(movie)

    # print(movie)
    # print(user_data)
    return user_data


# TESTING add_to_watched()
# user_data = { "watched": []}
# movie = {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}

# add_to_watched(user_data, movie)


def add_to_watchlist(user_data, movie):
    """
    Input: 
    user_data = {"watchlist":["Spider-man: No Way Home", "Dune"]}
    movie = { "title": "Title A", "genre": "Horror", "rating": 3.5}

    """
    # Add movie to the "watchlist" inside of user_data
    # return user_data

    if "watchlist" in user_data:
        user_data["watchlist"].append(movie)
    
    return user_data


def watch_movie(user_data, title):
    """
    Input: 
    user_data = {"watchlist" : ["Spider-man: No Way Home", "Dune"], "watched" : ["Star Wars", "Black Panther"]}
    title = "Iron Man 2"

    Output: return user_data
    """
    # title = string of movie title the user has watched

    # TASK ONE: search for title in user_data dictionary 
    # --> access with key "watchlist", look through list of movie titles

    # TASK TWO 
    # If you find it, remove the movie title from watchlist and add it to watched

    # TEST EIGHT: need to account for duplicate title names --> can only have unique title names

    
    # TEST SEVEN: dictionary where key = string, value = list of dictionaries
    # janes_data = {
    #     "watchlist": [{
    #         "title": MOVIE_TITLE_1,
    #         "genre": GENRE_1,
    #         "rating": RATING_1
    #     }],
    #     "watched": []
    # }

    # # Act
    # updated_data = watch_movie(janes_data, MOVIE_TITLE_1)

    for val in user_data["watchlist"]:
        
        if title == val:
            # print("YES!")

            user_data["watchlist"].remove(title)
            user_data["watched"].append(title)
    
    return user_data

    # print("watchlist:  ", user_data["watchlist"])

    # print("watched: ", user_data["watched"])






    # if title in user_data["watchlist"]:
    #     # print("yes!")
    #     user_data["watchlist"].remove(title)
    #     user_data["watched"].append(title)
    #     return user_data
    # else:
    #     return user_data

    # print("watchlist:", user_data["watchlist"])
    # print("watched:", user_data["watched"])
    # print(user_data)
    


# TESTING!!
user_data = {"watchlist" : ["Spider-man: No Way Home", "Dune", "Iron Man 2"], "watched" : ["Star Wars", "Black Panther"]}
title = "Iron Man 2"

watch_movie(user_data, title)

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

