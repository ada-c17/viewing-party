# ------------- WAVE 1 --------------------

from pickle import NONE
import copy

def create_movie(title, genre, rating):
    if not (title and genre and rating): # if title or genre or rationg is None return None
        return None
    
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    
    return new_movie

def add_to_watched(user_data, movie):
    
    for watched in user_data:
        user_data[watched] = [movie]     
    
    return user_data

def add_to_watchlist(user_data, movie):

    for watchlist in user_data:
        user_data[watchlist] = [movie]     
    
    return user_data

    

def watch_movie(user_data, title):
    # will use deep copy of user data to iterate over it
    # (since we are modifying user_data)
    user_data_deep_copy = copy.deepcopy(user_data)
    # if the "title" is in the movie in the watchlist, then add movie to watched and remove from watchlist
    #if the "title" is not in the movie in the watchlist, then return user_data

    
    # outer loop goes through list of movies in "watchlist"
    for movie in user_data_deep_copy["watchlist"]: 
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if user_data["watched"] == []: # watched list of movies is empty
            return 0.0
    average_rating = [] #list to keep rating of each movie

    # add rating of each movie to "average_rating" list
    # loop go through list of movies in watched list
    for movie in user_data["watched"]:
        average_rating.append(movie["rating"])
    return sum(average_rating) / len(average_rating)


def get_most_watched_genre(user_data):
    if user_data["watched"] == []: # empty user's watched list
            return None
    
    genre_dict = {} # dictionary to keep genre and it's frequentcy, example {"fantasy": 2, "horror": 1, "action":5}

    #1 get all genres and their frequency from user_data
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict: # if genre is not yet in dictionary, set its frequency to 1
            genre_dict[movie["genre"]] = 1
        else:
            genre_dict[movie["genre"]] += 1 # if genre is already in dictionary, increase frequency by 1

    #2 get the key with max value
    for genre in genre_dict:
        if genre_dict[genre] == max(genre_dict.values()):
            return genre 
    # max_rating = max(genre_dict.values())
    # most_genre = list(genre_dict.keys())[list(genre_dict.values()).index(max_rating)]
    # return most_genre

    
    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched = []
    unique_watched_user = []

    #get movies friends watched
    # outer loop goes through list of friends of user
    for friend in user_data["friends"]:
        # inner loop goes through list of friend's watched movies 
        for friend_movie in friend["watched"]:
            friends_watched.append(friend_movie)

    # get unique movies for user (that movies friends didn't watch)
    #add user movie to list of dictionaries if user's watched title not in the list of friend watched titles
    for user_movie in user_data['watched']:
        if user_movie not in friends_watched:
            unique_watched_user.append(user_movie)
    
    return unique_watched_user


def get_friends_unique_watched(user_data):
    user_watched = []
    friends_unique_movies = []
    # get the list of movies user watched
    for movie in user_data["watched"]:
        user_watched.append(movie)

    # get the list of movies friends watched but user not
    # outer loop goes through list of friends of user
    for friend in user_data["friends"]:
        # inner loop goes through list of friend's watched movies
        for friend_movie in friend["watched"]:
            if friend_movie not in user_watched:
                if friend_movie not in friends_unique_movies:
                    friends_unique_movies.append(friend_movie)

    return friends_unique_movies


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_watched_not_empty = False # use flag. If flag becomes True, means at least 1 friend has watched movie
    if user_data["watched"] == []: #if user_data "watched" is empty, return empty list []
        return []
    recommendations = []
    # outer loop goes through list of friends of user
    for friend in user_data["friends"]:
        if len(friend["watched"]) > 0: # check friend's "watched" is not empty
                friend_watched_not_empty = True
        # inner loop goes through list of friend's watched movies
        for friend_movie in friend["watched"]:
            if friend_movie not in user_data["watched"] and friend_movie["host"] in user_data["subscriptions"]:
                recommendations.append(friend_movie)

    if friend_watched_not_empty == False:  #if friends "watched" is empty, recommendations is empty
        recommendations = []
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    # get the user's most frequently watched genre
    # get list of recommended movies
    # get_available_recs() function will return the list of recommended movies user didn't watched yet and at least on of friend has watched movie
    # remove from the list of recommended movies the movie which genre is not most watched user genre
    if user_data["watched"] == []:
        return []
    user_most_watched_genre = get_most_watched_genre(user_data)
    new_rec_movies = get_available_recs(user_data)
    for movie in new_rec_movies:
        if movie["genre"] != user_most_watched_genre:
            new_rec_movies.remove(movie)

    return new_rec_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []
    # recommended_movies = get_new_rec_by_genre(user_data)
    friends_watched = []
    if not user_data["favorites"]: #if user's "Favorite" list is empty just return recommended empty movies list
        return recommended_movies

    # get the list friends watched movies
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_watched.append(friend_movie)

    # if user's favorite movie not in the friends watched list add movie to recommended list
    for user_favorite_movie in user_data["favorites"]:
        if user_favorite_movie not in friends_watched:
            recommended_movies.append(user_favorite_movie)

    return recommended_movies


