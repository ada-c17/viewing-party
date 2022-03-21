# ------------- WAVE 1 --------------------

from tests.test_constants import USER_DATA_5
import copy

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {"title" : title,
                "genre" : genre,
                "rating" : rating}
    return movie

def add_to_watched(user_data, movie):
    # make deep copy of original data and modifying that instead of modifying user_data in place
    # because consuming unit tests expect a return value
    copied_user_data = copy.deepcopy(user_data)
    copied_user_data["watched"].append(movie)
    return copied_user_data

def add_to_watchlist(user_data, movie):
    copied_user_data = copy.deepcopy(user_data)
    copied_user_data["watchlist"].append(movie)
    return copied_user_data

def watch_movie(user_data, movie_title):
    copied_user_data = copy.deepcopy(user_data)
    for movie in copied_user_data["watchlist"]:
        if movie["title"] == movie_title:
            copied_user_data["watched"].append(movie)
            copied_user_data["watchlist"].remove(movie)
    return copied_user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    # use try, except in case there is no data in user_data["watched"]
    try:
        ave_rating = total_rating / len(user_data["watched"])
    except ZeroDivisionError:
        ave_rating = 0
    return ave_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data["watched"]:
        watched_genre = movie["genre"]
        if watched_genre in genre_dict:
            genre_dict[watched_genre] += 1
        else:
            genre_dict[watched_genre] = 0
    # use try, except in case there is no value for most_watched_genre        
    try:
        most_watched_genre = max(genre_dict, key=genre_dict.get)
    except ValueError:
        most_watched_genre = None
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # get the list of movies that all friends watched
    friends_watched_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie in friends_watched_movie:
                friends_watched_movie.append(movie)
    # get user's unique watched movies by checking if same movie is in friend's watched list
    unique_watched_movie = []
    for movie in user_data["watched"]:
        if not movie in friends_watched_movie and not movie in unique_watched_movie:
            unique_watched_movie.append(movie)
    
    return unique_watched_movie

def get_friends_unique_watched(user_data):
    friends_uniqute_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie in user_data["watched"] and not movie in friends_uniqute_watched:
                friends_uniqute_watched.append(movie)

    return friends_uniqute_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []
    # get movies that only friends watched
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        # use try, except in case there is no key 'subscriptions'
        try:
            if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
        except KeyError:
            # don't recommend a move if it is not available on any of the user's subscriptions
            pass
    return recommendations




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommendations_genre = []
    # get most watched genre of user 
    most_watched_genre_of_user = get_most_watched_genre(user_data)
    # get possible recommendations for user
    possible_recs = get_available_recs(user_data) 
    for movie in possible_recs:
        # add movie if genre is equal to user's most watched genre and if it is not recommended yet
        if movie["genre"]== most_watched_genre_of_user and not movie["genre"] in recommendations_genre:
            recommendations_genre.append(movie)

    return recommendations_genre

def get_rec_from_favorites(user_data):
    recommendations_fav = []
    # get user's favorite movies
    user_favorites = user_data["favorites"]
    # get movies that only user watched
    user_unique_watched = get_unique_watched(user_data)
    for movie in user_favorites:
        if movie in user_unique_watched:
            recommendations_fav.append(movie)
        
    return recommendations_fav
        

