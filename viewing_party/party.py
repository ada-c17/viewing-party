
# ------------- WAVE 1 --------------------

from logging.handlers import WatchedFileHandler


def create_movie(title, genre, rating):
    '''
    this function adds movie details to dictionary and returns movie details.
    if title is None, function returns None.
    '''
    new_movie = {
        "title": title,
        "genre":genre,
        "rating": rating
    }

    if title == None or genre == None or rating == None:
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
    '''
    this function adds movie data in the form of a dictionary
    to a dictionary of user_data, where the key is watched and
    the values are a list of dictionaries of movies the user has watched
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    this function adds movie data in the form of a dictionary
    to a dictionary of user_data, where the key is watchlist and
    the values are a list of dictionaries of movies the user has queued to watch
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    this function will move a movie from watchlist to watched
    '''
    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].pop()
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''
    this function calculates the average rating of the
    movies in the watched list
    '''
    num_movies_watched = 0
    rating_sum = 0
    for lst_name, lst_contents in user_data.items():
        num_movies_watched += len(lst_contents)
        for movie in lst_contents:
            rating_sum += movie["rating"]

    if num_movies_watched == 0:
        average_rating = 0
    else:
        average_rating = rating_sum/num_movies_watched

    return average_rating

def get_most_watched_genre(user_data):
    '''
    this function returns the genre most
    frequently listed in the watched list
    '''
    user_genre_count = {}

    if len(user_data["watched"]) == 0:
        most_watched_genre = None    
    else:
        for movie in user_data["watched"]:
            genre = movie["genre"]

            if genre not in user_genre_count.keys():
                user_genre_count[genre] = 1
            else:
                user_genre_count[genre] += 1
        
        most_watched_genre = max(user_genre_count, key=user_genre_count.get)
    
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    '''
    this function compares a user's watched movie list
    to their friends' watched movies lists and
    returns a list of unique movies the user has watched
    '''

    user_all_movies = []
    friends_all_movies = []
    user_unique_movies = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_all_movies.append(friend_movie["title"])

    for movie in user_data["watched"]:
        user_all_movies.append(movie["title"])

    for title in user_all_movies:
        if not title in friends_all_movies:
            unique_movie = title
            for movie in user_data["watched"]:
                if unique_movie == movie["title"]:
                    user_unique_movies.append(movie)

    return user_unique_movies

def get_friends_unique_watched(user_data):
    '''
    this function compares a user's watched movie list
    to their friends' watched movies lists and
    returns a list of unique movies the user's friends have watched
    '''
    user_all_movies = []
    friends_all_movies = []
    friends_unique_movies = []

    for movie in user_data["watched"]:
        user_all_movies.append(movie["title"])

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if not friend_movie["title"] in friends_all_movies:
                friends_all_movies.append(friend_movie["title"])

    for title in friends_all_movies:
        if not title in user_all_movies:
            friend_unique_movie = title

            for friend in user_data["friends"]:
                for friend_movie in friend["watched"]:
                    if friend_unique_movie == friend_movie["title"] \
                        and not friend_movie in friends_unique_movies:
                        friends_unique_movies.append(friend_movie)

    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''
    this function returns a list of recommended movies
    that the user has not watched and at least
    one of the users friends has watched, while
    the host of the movie is a service the user
    is subscribed to
    '''

    movie_recommendations = []

    friend_unique_movies = get_friends_unique_watched(user_data)

    for movie in friend_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            movie_recommendations.append(movie)

    return movie_recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------