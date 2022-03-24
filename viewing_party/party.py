# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    # create dictionary with specific keys
    new_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # check if statement with the value, if it is truthy
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        return new_dict
    # if it is falsy return None
    else: 
        return None

def add_to_watched(user_data, movie):
    # check the length of user_data == 1
    if len(user_data) == 1:
        # if it is true then add movie to user_data dictionary with "watched" key
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    # check the length of user_data == 1
    if len(user_data) == 1:
        # if it is true, then add movie to user_data dictionary with "watchlist" key
        user_data["watchlist"].append(movie)
        return user_data


def watch_movie(user_data, title):
    # iteratable through user_data["watchlist"]
    for movie in user_data["watchlist"]:
        # check if movie title key == to title
        if movie["title"] == title:
            # if it is true, then remove movie from 'watchlist' key
            user_data["watchlist"].remove(movie)
            # then add movie to "watched" key
            user_data["watched"].append(movie)
            return user_data
    return user_data
        



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # we want to find the average rating of all movies
    # using list comprehension to variable ratings
    #iterate in user_data with watched key to check the ratings
    ratings = [movie["rating"] for movie in user_data["watched"]]
    # checking the length of user_data of 'watched' key
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        #calculating the average rating of all movies
        return sum(ratings) / len(ratings)


def get_most_watched_genre(user_data):
    # check the length of user_data['watched']
    if len(user_data["watched"]) == 0:
        return None
    else:
        # create empty dictionary
        frequently = {}
        # iterate in user_data of 'watched' key to find the most genres occurring
        genres = [movie["genre"] for movie in user_data["watched"]]
        # iterate in genres
        for genre in genres:
            # check if the genre in frequently or not
            if genre in frequently:
                # if yes then increment by 1
                frequently[genre] += 1
            else:
                # if already have
                frequently[genre] = 1
        # find the most occurring of genres
        popular = max(frequently, key=frequently.get)
        return popular

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
 #find unique list of movie of user that their friend hasnt watch yet
    
    # using list comprehensions
    friend_movies = [num_friends for friend in user_data["friends"] for num_friends in friend["watched"]]
    unique_user_movies = [movie for movie in user_data["watched"] if not movie in friend_movies]
    return unique_user_movies


    # initializes empty list to friend_movies
    #unique_user_movies = []
    #friend_movies = []
    #iterate in user_data dictionary of 'friends' key
    #for friend in user_data["friends"]:
        # add friend['watched'] to friend_movies list
        #friend_movies.extend(friend["watched"])
    
    # iterate in user_data dictionary of 'watched' key
    #for movie in user_data["watched"]:
        # check if movie not in friend_movies
        #if not movie in friend_movies:
            # add movie to unique_user_movies list
            #unique_user_movies.append(movie)
    
    #return unique_user_movies

def get_friends_unique_watched(user_data):
  #find the unique list of movie of friends that user hasnt watch yet
    unique_friend_movies = []
    
    #iterate through user_data dictionary with 'friends' key
    for friend in user_data["friends"]:
        #iterate through watched key
        for movie in friend["watched"]:
            # if movie not in user_data dictionary and unique_friend_movies list
            if not movie in user_data["watched"] and not movie in unique_friend_movies:
                # add movie to unique_friend_movies list
                unique_friend_movies.append(movie)
            
            
    return unique_friend_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    # finding a list of recommended movies and add to the list if user has not watched but one of user friend has watched
    # using the list comprehension
    # iterate in user_data['friends'] and into friend['watched']
    friends_movies = [movie for friend in user_data["friends"] for movie in friend["watched"]]
    # iterate in friend_movies list to check if movie not in user_data['watched'] and movies['host'] key in user_data['subscriptions']
    recommended_movies = [movie for movie in friends_movies if not movie in user_data["watched"] if movie["host"] in user_data["subscriptions"]]
    return recommended_movies



    # recommended_movies = []
    # friends_movies = []
    # for friend in user_data["friends"]:
    #     friends_movies.extend(friend["watched"])

    # for movie in friends_movies:
    #     if not movie in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
    #         recommended_movies.append(movie)
    # return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    #using helper functions
    # movies that user has not watch yet
    popular_genre = get_most_watched_genre(user_data)
    # movies that at least one of the user's friends has watched
    user_not_watched = get_friends_unique_watched(user_data)
    # finding the list of recommend movies with help functions
    recommended_movies = [movie for movie in user_not_watched if popular_genre is not None if movie['genre'] in popular_genre]
    return recommended_movies


    # recommended_movies = []
    # popular_genre = get_most_watched_genre(user_data)
    # user_not_watched = get_friends_unique_watched(user_data)

    # if popular_genre is not None:
    #     for movie in user_not_watched:
    #         if movie["genre"] in popular_genre:
    #             recommended_movies.append(movie)
    
    # return recommended_movies


def get_rec_from_favorites(user_data):

    #using helper function from wave 3 of list of movies that user has watched but none of user friends watched
    unique_watched = get_unique_watched(user_data)
    # finding the user favorites list of movies
    rec_movies = [movie for movie in unique_watched if movie in user_data["favorites"]]
    return rec_movies


    # rec_movies = []
    # unique_watched = get_unique_watched(user_data)
    # for movie in unique_watched:
    #     if movie in user_data["favorites"]:
    #         rec_movies.append(movie)
    # return rec_movies
        
    
    
    

