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
    user_data = {'watchlist': [{'title': 'The Lord of the Functions: The Fellowship of the Function','genre': 'Fantasy', 'rating': 4.8}], 
        'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}]}
    title = "Iron Man 2"

    Output: return user_data
    """
    # title = string of movie title the user has watched

    # TASK ONE: search for title in user_data dictionary 
    # --> access with key "watchlist", look through list of movie titles

    # TASK TWO 
    # If you find it, remove the movie title from watchlist and add it to watched

    for key, val in user_data.items():
        # Loop enters dictionary and checks for the "watchlist" key
        if key == "watchlist":
            # If the "watchlist" key is in the dictionary, access the "watchlist" dictionary

            for category in user_data[key]:
                # Loop through the list value of the "watchlist" key 

                if title == category["title"]:
                    # If title is in the inner dictionary as a key, loop enters the dictionary inside the list
                    
                    move_movie = (user_data[key][0])
                    user_data[key].pop(0)

                    if move_movie not in user_data["watched"]:
                        # If the movie title isn't already in the "watched" list, add the title
                        # Can't have duplicate names
                        user_data["watched"].append(move_movie)

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # Calculate the average rating of all the movies in the watched list
        # Empty list average rating is 0.0
    # Return average rating
    total = 0
    count = 0
    
    for category in user_data:
        # print(user_data[category])
        if category == "watched":
            # print(user_data[category])
            for val in user_data[category]:
                # print(user_data[category])
                for info in val:
                    
                    if info == "rating":
                        # print(val[info])
                        total += val[info]
                        count += 1
    
    ave_rating = float(total/count)
    return ave_rating


# TESTING!!

# user_data = {'watchlist': [{'title': 'The Lord of the Functions: The Fellowship of the Function','genre': 'Fantasy', 'rating': 4.8}], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}]}
# title = 'The Lord of the Functions: The Fellowship of the Function'

# watch_movie(user_data, title)
# # # output from watch_movie:
# # # {'watchlist': [], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}]}
# get_watched_avg_rating(user_data)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

