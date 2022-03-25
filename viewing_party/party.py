
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    adds movie details to dictionary and returns movie details
    if title, genre, or rating are None, function returns None
    '''
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if title is None or genre is None or rating is None:
        return None
    elif title == False or genre == False or rating == False:
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
    '''
    adds movie data in the form of a dictionary
    to a dictionary of user_data, where the key is watched and
    the values are a list of dictionaries of movies the user has watched
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    adds movie data in the form of a dictionary
    to a dictionary of user_data, where the key is watchlist and
    the values are a list of dictionaries of movies the user has queued to watch
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    moves a movie from watchlist to watched
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
    calculates the average rating of the movies in the watched list
    '''

    total_movies_watched = len(user_data["watched"])
    rating_total = 0

    for movie in user_data["watched"]:
        rating_total += movie["rating"]

    if total_movies_watched == 0:
        average_rating = 0
    else:
        average_rating = rating_total/total_movies_watched

    return average_rating

def get_most_watched_genre(user_data):
    '''
    returns the genre most frequently listed in the watched list
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
    compares a user's watched movie list to their friends' watched movies lists 
    and returns a list of unique movies the user has watched
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
    compares a user's watched movie list to their friends' watched movies lists and
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
    returns a list of movies that the user has not watched 
    and at least one of the users friends has watched, while
    the host of the movie is a service the user is subscribed to
    '''

    movie_recommendations = []

    friend_unique_movies = get_friends_unique_watched(user_data)

    if user_data["watched"]:
        for movie in friend_unique_movies:
            if movie["host"] in user_data["subscriptions"]:
                movie_recommendations.append(movie)

    return movie_recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''
    returns a list of recommended movies of the genre most frequently watched by the user, 
    that the user has not watched, and at least one of the user's friends has watched 
    '''

    movie_recommendations_by_genre = []

    user_most_watched_genre = get_most_watched_genre(user_data)

    recommendation_list = get_available_recs(user_data)

    for movie in recommendation_list:
        if movie["genre"] == user_most_watched_genre:
            movie_recommendations_by_genre.append(movie)

    return movie_recommendations_by_genre

def get_rec_from_favorites(user_data):
    '''
    returns a list of recommended movies from movies in the user's favorites list, 
    which the user's friends have not watched 
    '''

    favorite_movie_recommendations = []

    user_unique_watched = get_unique_watched(user_data)

    for movie in user_unique_watched:
        if movie in user_data["favorites"]:
            favorite_movie_recommendations.append(movie)

    return favorite_movie_recommendations
