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


# TESTING!!
# user_data = { "watched": []}
# movie = {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}

# add_to_watched(user_data, movie)


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

