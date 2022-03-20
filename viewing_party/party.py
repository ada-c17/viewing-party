from collections import Counter
import copy

def create_movie(title, genre, rating):
    # If title, genre, or rating are "None", return None, otherwise create movie
    if title == None or genre == None or rating == None:
        movie = None
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    
    return movie

def add_to_watched(user_data, movie):
    # Add movie to user's "watched" list
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # Add movie to user's watchlist
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # Move movie from user's watchlist to watched
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # Calculate average rating for movie in user's "watched" list
    sum_ratings = 0
    count_ratings = 0

    for movie in user_data["watched"]:
        sum_ratings += movie["rating"]
        count_ratings += 1

    if user_data["watched"] == []:
        avg_rating = 0
    else:
        avg_rating = sum_ratings / count_ratings

    return avg_rating

def get_most_watched_genre(user_data):
    # Find most watched genre
    if user_data["watched"] == []:
        most_watched_genre = None
    else:
        genre_list = []

        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])
        
        # Get list of frequencies of each genre
        frequency = Counter(genre_list)

        # Find most frequent genre name
        most_watched_genre = frequency.most_common(1)[0][0]

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    '''
    Get list of movies the user watched that none of their friends have watched
    '''
    user_unique_watched = []
    for movie in user_data["watched"]:
        movie_unique = True
        for friend in range(len(user_data["friends"])):
            if movie in user_data["friends"][friend]["watched"]:
                movie_unique = False
        if movie_unique == True:
            user_unique_watched.append(movie)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    '''
    Get list of movies any of the user's friends watched but the user has not
    '''
    friends_unique_watched = []
    for friend in range(len(user_data["friends"])):
        for movie in user_data["friends"][friend]["watched"]:
            if movie not in friends_unique_watched:
                movie_unique = True
                if movie in user_data["watched"]:
                    movie_unique = False
                if movie_unique == True:
                    friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''
    Get list of movie recommendations that any of the user's friends have
    watched but that the user has not. Excludes movies available on a
    host/subscription service that the user does not have access to.
    '''
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommendations = []
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)
    
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''Get movie recommendations that match the user's most watched genre'''
    # Get movies unique to friends (user hasn't watched)
    # available_recommendations = get_available_recs(user_data) <--using this 
    # instead of the following line requires user_data to have "subscriptions"
    available_recommendations = get_friends_unique_watched(user_data)
    
    # Get user's most watched genre
    most_watched_genre = get_most_watched_genre(user_data)

    # For each movie in the recommendation list that is the user's most
    # watched genre, add it to the recommendations by genre list
    recs_by_genre = []
    for movie in available_recommendations:
        if movie["genre"] == most_watched_genre:
            recs_by_genre.append(movie)
    
    return recs_by_genre

def get_rec_from_favorites(user_data):
    '''
    Recommend list of movies the user has watched that is in their favorites
    list when their friends have not watched the movie.
    '''
    user_unique_watched = get_unique_watched(user_data)
    recommended = []
    for movie in user_unique_watched:
        if movie in user_data["favorites"]:
            recommended.append(movie)

    return recommended