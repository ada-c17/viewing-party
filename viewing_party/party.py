# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        movie_data = None

    else:
        movie_data = {
            'title': title,
            'genre': genre,
            'rating': rating
            }
            
    return movie_data


def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """Returns the average rating of the user's watched movies."""
    try:
        total = 0
        for movie in user_data["watched"]:
            total += movie['rating']
        average = total / len(user_data["watched"])

    except ZeroDivisionError:
        average = 0.0

    return average


def get_most_watched_genre(user_data):
    """Returns user's most watched genre."""
    if user_data["watched"]:
        # Iterates over the movies in the user's watched list and adds the movie genre into a list
        genre_list = [movie["genre"] for movie in user_data["watched"]]
        # Find the most frequent movie genre
        most_popular_genre = max(genre_list, key = genre_list.count)
    else:
        most_popular_genre = None

    return most_popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_watched_movies(user_data):
    """Returns a list of the friends' watched movies."""
    friends_watched_movies = []
    # Uses range to loop over the friends
    for index in range(len(user_data["friends"])):
        # for each friend, if the movie is not in friends_watched_movies, add the movie to the friends_watched_movies
        if user_data["friends"][index]["watched"] not in friends_watched_movies:
            friends_watched_movies += user_data["friends"][index]["watched"]
    
    return friends_watched_movies


def get_user_watched_movies(user_data):
    """Returns a list of the user's watched movies."""
    user_watched_movies = []
    # Loops over each movie in the user's watched movies
    for movie in range(len(user_data["watched"])):
        if user_data["watched"][movie] not in user_watched_movies:
            # if the movie is not in the user_watched_movies, add the movie to user_watched_movies
            user_watched_movies.append(user_data["watched"][movie])
    
    return user_watched_movies


def get_unique_watched(user_data):
    '''
    Determines which movies the user has watched, but none of their friends have watched.

    Returns:
    unique_watched_movies (list): Each movie represents a dictionary.
    '''
    unique_watched = []

    friends_watched_movies = get_friends_watched_movies(user_data)
    user_watched_movies = get_user_watched_movies(user_data)

    for movie in user_watched_movies:
        if (movie not in friends_watched_movies) and (movie not in unique_watched):
            unique_watched.append(movie)
    
    return unique_watched
    

def get_friends_unique_watched(user_data):
    '''
    Determines which movies at least one of the user's friends have watched, but the user has not watched.
    
    Returns:
    friends_unique_watched (list): Each movie represents a dictionary.
    '''
    friends_unique_watched = []

    friends_watched_movies = get_friends_watched_movies(user_data)
    user_watched_movies = get_user_watched_movies(user_data)

    for movie in friends_watched_movies:
        if (movie not in user_watched_movies) and (movie not in friends_unique_watched):
            friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    Determines recommended movies if the user has not watched it, the movie is a host of the user, and at least one friend has watched the movie. 

    Returns:
    available_recs (list): Each movie represents a dictionary.
    '''
    available_recs = []

    friends_watched_movies = get_friends_watched_movies(user_data)
    user_watched_movies = get_user_watched_movies(user_data)

    for movie in friends_watched_movies:
        if (movie not in user_watched_movies) and (movie["host"] in user_data["subscriptions"]) and (movie not in available_recs):
            available_recs.append(movie)

    return available_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    '''
    Determines recommended movies based on the user's most frequently watched genre.

    Returns:
    new_rec_by_genre (list): Each movie represents a dictionary.
    '''
    friends_watched_movies = get_friends_watched_movies(user_data)
    user_watched_movies = get_user_watched_movies(user_data)
    pass
    user_most_watched_genre = get_most_watched_genre(user_data)

    new_rec_by_genre = []    

    for movie in friends_watched_movies:
        if (movie not in user_watched_movies) and (movie["genre"] == user_most_watched_genre) and (movie not in new_rec_by_genre):
            new_rec_by_genre.append(movie)
    
    return new_rec_by_genre


def get_rec_from_favorites(user_data):
    '''
    Determines a list of recommended movies from the user's favorite movies. 

    Returns:
    rec_from_favorites (list): Each movie represents a dictionary. 
    '''   
    friends_watched_movies = get_friends_watched_movies(user_data)

    rec_from_favorites = []

    for movie in user_data["favorites"]:
        if movie not in friends_watched_movies and movie not in rec_from_favorites:
            rec_from_favorites.append(movie)
    
    return rec_from_favorites