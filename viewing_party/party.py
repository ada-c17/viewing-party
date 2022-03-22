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
    """
    Input: user_data = dictionary of lists (watched list and watch list)
    Output: average movie rating (float)
    """

    # Calculate the average rating of all the movies in the watched list
        # Empty list average rating is 0.0
    # Return average rating

    total = 0
    count = 0
    ave_rating = 0
    
    for category in user_data:
        # Loop enters dictionary 

        if category == "watched":
            # Checking for "watched" list
            # If the "watched" key is found, step into the "watched" list

            if not user_data[category]:
                # If the "watched" list is empty, set average rating to 0.0
                total += 0.0
                count += 1
                ave_rating = 0.0

            else:
                # user_data at this point: [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}]
                for val in user_data[category]:
                    # Loop enters the "watched" list

                    for info in val:
                        # Loop through the different movie information

                        if info == "rating":
                            # print(val[info])
                            total += val[info]
                            count += 1
    
    ave_rating = float(total/count)
    return ave_rating


def get_most_watched_genre(user_data):
    """
    Input: user_data = dictionary with a 'watched' list of movie dictionaries
    Output: most popular movie genre
    """
    seen_genre = []
    most_popular_genre = 0
    
    
    for category in user_data:
    # Loop enters dictionary 

        if category == "watched":
        # Checking for "watched" list

            if not user_data[category]:
                # If the "watched" list is empty, return most_popular_genre as None
                most_popular_genre = None
                return most_popular_genre
            else:
                for item in user_data[category]:
                    # If the "watched" list isn't empty, loop through the "watched" list
                    # Loop enters "watched" list which contains dictionaries
                    
                    for movie_info in item:
                        # Looping through the different movie information like: title, genre, rating

                        if movie_info == "genre":
                            # Get the genre info and append to the empty list seen_genre
                            seen_genre.append(item[movie_info])

                most_popular_genre = max(set(seen_genre), key = seen_genre.count)
                # Find the most frequent element in the list, this is the most popular genre

    return most_popular_genre


# TESTING!!
# EMPTY LIST:
# user_data = {'watchlist': [{'title': 'The Lord of the Functions: The Fellowship of the Function','genre': 'Fantasy', 'rating': 4.8}], 'watched': []}

# NORMAL LIST:
# user_data = {'watchlist': [], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}]}
# title = 'The Lord of the Functions: The Fellowship of the Function'

# watch_movie(user_data, title)
# output from watch_movie before calling get_watched_avg_rating(user_data):
# {'watchlist': [], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}]}

# get_watched_avg_rating(user_data)

# get_most_watched_genre(user_data)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

