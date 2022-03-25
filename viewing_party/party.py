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

    count = 0
    movie_ratings = []

    movies_watched = user_data["watched"]
    # Get the "watched" list from inside the dictionary

    if len(movies_watched) == 0:
        # If the "watched" list is empty, return an average rating of 0.0
        return 0.0
    else:
        for movie in movies_watched:
            # If the "watched" list isn't empty, loop enters the list value of dictionaries
            if movie["rating"]:
                # If inner dictionary (inside the list value) has a key of "rating"
                # Count that it's there and append the rating value to the movie_ratings list
                count += 1
                movie_ratings.append(movie["rating"])
        # Return average movie rating
        return float(sum(movie_ratings)/count)


def get_most_watched_genre(user_data):
    """
    Input: user_data = dictionary with a 'watched' list of movie dictionaries
    Output: most popular movie genre
    """
    seen_genre = []
    
    
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



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    Input: user_data = dictionary with "watched" list of movie dictionaries 
        and "friends" is a list with each item as a dictionary
    Output: return list of dictionaries --> unique_list
    """
    # List of movies user has watched
    # List of movies friends have watched
    # Find movies the user has watched but friends HAVEN'T
    # Return a list of dictionaries --> list of movies

    # List of movies friends have watched
    # the elements are dictionaries with lists of dictionaries are the values
    friend_list = user_data["friends"]

    # List of movies the user has watched
    # the elements are dictionaries (one dictionary, one movie)
    user_list = user_data["watched"]
    
    # Empty list to put movies only the user has seen
    user_unique_list = []
    # Empty list to populate with --> want to flatten the friend_list so that list of dictionaries (one dictionary, one movie)
    friends_movies = []


    # Flatten friend_list so that its a list of dictionaries
    for friend_movie in friend_list:
        # Loop enters the inner list with two "watched" dictionaries
        for film in friend_movie["watched"]:
            # Loop through the dictionaries in the two "watched" dictionaries 
            friends_movies.append(film)
            # Append a dictionary to the empty friends_movies so that its a list of dictionaries

    
    for movie in user_list:
        # Loop through the user_list (list of dictionaries)
        if (movie not in friends_movies) and (movie not in user_unique_list):
            # Find the movies that only the user has watched
            user_unique_list.append(movie)
            
    return user_unique_list


def get_friends_unique_watched(user_data):
    """
    Input: user_data = dictionary with "watched" list of movie dictionaries 
        and "friends" is a list with each item as a dictionary
    Output: return list of dictionaries where each dictionary is a movie 
    """

    # List of movies friends have watched
    # the elements are dictionaries with lists of dictionaries are the values
    friends_data = user_data["friends"]

    # List of movies the user has watched
    # the elements are dictionaries (one dictionary, one movie)
    user_movie_list = user_data["watched"]

    # Empty list to populate with --> want to flatten the friend_list so that list of dictionaries (one dictionary, one movie)
    friend_movie_list = []
    
    # Empty list to put movies only the friends have seen
    friend_unique_list = []



    # Flatten friend_list so that its a list of dictionaries
    for friend_film in friends_data:
        # Loop through inner list that has two "watched" dictionaries
        for film in friend_film["watched"]:
            # Append a dictionary to the empty friends_movies so that its a list of dictionaries
            friend_movie_list.append(film)


    for movie in friend_movie_list:
        # Loop through the user_list (list of dictionaries)
        if (movie not in user_movie_list) and (movie not in friend_unique_list):
            # Movie not in user list --> add to friends unique list
            friend_unique_list.append(movie)
    
    return friend_unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    Input: user_data = dictionary with "watched" list of movie dictionaries 
        and "friends" is a list with each item as a dictionary
    Output: return list of recommended movies
    """
    # List of movies friends have watched
    # the elements are dictionaries with lists of dictionaries are the values
    friend_list = user_data["friends"]

    # List of movies the user has watched
    # the elements are dictionaries (one dictionary, one movie)
    user_list = user_data["watched"]

    # User's subscriptions services
    user_subscriptions = user_data["subscriptions"]

    # Empty list to populate with --> want to flatten the friend_list 
    # so that list of dictionaries (one dictionary, one movie)
    friend_movie_list = []



    for friend in friend_list:
        # Loop through the inner list that has two "watched" dictionaries
        for movie in friend["watched"]:
            # For each film in the "watched" dictionaries, append to the empty list
            friend_movie_list.append(movie)


    # List of recommended movies
    #   --> User has NOT watched it
    #   --> A least ONE FRIEND has seen it
    #   --> "host" of the movie is a service in the USERS "subscriptions"
    recommended_list = []

    for film in friend_movie_list:
        # Loop through each film in friend_movie_list
        if (film not in user_list) and (film in friend_movie_list):
            if film["host"] in user_subscriptions:
                # If the film meets these criteria, add to recommended list
                recommended_list.append(film)
    
    return recommended_list



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    """
    Input: user_data = dictionary with "watched" list of movie dictionaries 
        and "friends" is a list with each item as a dictionary
    Output: return list of recommended movies
    """

    # TASK ONE: parse through User's data --> get movie titles and genres
    # TASK TWO: from user's genres --> find most popular genre
    # TASK THREE: find movies that user has NOT watched, a friend HAS watched,
                # and is of user's most popular genre (TASK TWO)

        # Add to recommended movies if:
        # User has not seen it
        # At least one friend has watched it
        # "genre" is the same as the user's most frequent genre


    # List of movies friends have watched
    # the elements are dictionaries with lists of dictionaries are the values
    friend_list = user_data["friends"]

    # List of movies the user has watched
    # the elements are dictionaries (one dictionary, one movie)
    user_list = user_data["watched"]



    # Get user's genre's --> find most popular genre
    users_genres =[]

    for title in user_list:
        users_genres.append(title["genre"])

    if len(users_genres) > 0:
        most_popular_genre = max(set(users_genres), key = users_genres.count)
    else: 
        most_popular_genre = 0



    # Empty list to populate with movies friends have seen
    friends_movies = []

    # Empty list to populate with movie recommendations
    movie_recs = []

    for friend in friend_list:
        if friend["watched"]:
            # If friends "watched" dictionary isn't empty, append movies to friends_movies list
            for film in friend["watched"]:
                friends_movies.append(film)
        else:
            # If friends "watched" dictionary is empty, return empty list
            return movie_recs


    for movie in friends_movies:
        # Loop through movies in friends_movies list
        if (movie not in user_list) and (movie["genre"] == most_popular_genre):
            # If movie meets these criteria, append to movie_recs list
            movie_recs.append(movie)
    
    return movie_recs



def get_rec_from_favorites():
    pass