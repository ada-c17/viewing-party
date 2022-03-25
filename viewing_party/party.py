# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """ creating movie dictionary and return movies of dictionary """

    # ditionary to store movies
    movies = {}

    # if any one of paramenters is None, function return None
    if title == None or genre == None or rating == None:
        return None

    # add movie into dictionary, if all paramenter is valid value or truthy
    elif title and genre and rating:
        
        movies["title"] = title
        movies["genre"] = genre
        movies["rating"] = rating
        return movies
    
    # Otherwise, return None.
    else:
        return None


def add_to_watched(user_data, movie):
    """ Adding movies into user data watched list and return user data"""

    # list to store watched movies
    watched_movies = []
    # add watched movies to a list
    watched_movies.append(movie)
    # add watched movies list into user data watched list
    user_data["watched"] = watched_movies
    return user_data


def add_to_watchlist(user_data, movie):
    """ Adding movies into user data watchlist and return user data """

    # list to store watchlist movies
    watchlist_movies = []
    # add watchlist movies to a list
    watchlist_movies.append(movie)
    # add watchlist movies list into user data watchlist
    user_data["watchlist"] = watchlist_movies
    return user_data


def watch_movie(user_data, title):
    """
    if the tile in the user's watchlist
        - remove movie from the watchlist
        - add movie to watched
        - return the user_data
    """
    # loop to get each movie in user watchlist for comparing with title
    for movie in user_data["watchlist"]:
        # if the title is in the user's movie watchlist 
        if title in movie["title"]:
            # add that movie into user's watched list
            user_data["watched"].append(movie)
            # remove that movie from user's watchlist
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    """Calculating the average of rating and return average rating"""
    
    # return 0 if user data watched is empty
    if len(user_data["watched"]) == 0:
        return 0

    # otherwise, calculating the average rating
    else:
        # assign 0 to total rating 
        sum_rating = 0
        # loop to get each value of user data watched list
        for movie in user_data["watched"]:
            # sum all rating of user data watched list
            sum_rating += movie["rating"]
        # calculate the average rating
        average_rating = sum_rating / len(user_data["watched"])
    return average_rating


def get_most_watched_genre(user_data):
    """ Finding most watched genre and return it """

    # return 0, if the user data watched is empty
    if len(user_data["watched"]) == 0:
        return None

    # otherwise, finding most watched genre
    else:
        # The list to store all genres
        genres = []
        # variable to find max counter of most watched genre 
        max_value = 0
        # variable to store most watched genre and return at the end
        most_watched_genre = ""

        # create a list to store all genres from user wathced
        # loop over each element of user watched to get genre 
        for movie in user_data["watched"]:
            # add genre into list
            genres.append(movie["genre"])

        # find the most watched genre
        # loop over the each element of genres list to get genre 
        for genre in genres:
            # count numbers of each genre in the list
            genre_count = genres.count(genre)
            # find the max counter of genre 
            if genre_count > max_value :
                # reassign the max_value as genre_count everytime when the if statement is true
                max_value = genre_count
                # assign genre name to most_watched_genre, it changes for every time the max_value been changed
                most_watched_genre = genre
            
        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_friends_watched_movie(user_data):
    """ Creating friend watched movie list from user data to analyze easier then return it. It is reuseable function. """

    # list to store all friend watched movies dictionary to compare with user wathced list
    friends_watched_list = []

    # loop to get the each friend watched moives
    for movie in user_data["friends"]:
        # extend whole list of each friend watched movie into new list
        friends_watched_list.extend(movie["watched"])

    return friends_watched_list


def get_unique_watched(user_data):
    """ check the list of movies of user watched list that are not in friend watched list then return it. """

    # assign user's friend watch list that is returning from get_friends_watched_movie function
    friends_watched_list = get_friends_watched_movie(user_data)

    # list of dictionary that store all movies are not in friend watched list
    user_unique_watched = []
            
    # compare user watched list and friends watched list
    # loop to get each movie dictionary of user watched list for comparing with friend watched list
    for movie in user_data["watched"]:

        
        # check if the movie that user has watched but none of their friends have wathced
        # add movie into a new list if it is not duplicate and return that new list at the end
        if movie not in friends_watched_list and movie not in user_unique_watched:
            user_unique_watched.append(movie)
    return user_unique_watched

    
def get_friends_unique_watched(user_data):      
    """ Finding the list of movies that user has no watched but user's friend had watched at least one then return it. """

    # assign user's friend watch list that is returning from get_friends_watched_movie function
    friends_watched_list = get_friends_watched_movie(user_data)

    # list of dictionary that store all movies are not in user watched list
    friend_unique_watched = []

    # compare user watched list and friends watched list
    # loop to get each movie dictionary of firend watched movies list for comparing with user watched list          
    for movie in friends_watched_list:

        # check if the movie that at least one of their friend have watched but the user has not watched
        # add that movie into a new list if it is not duplicate and return that new list at the end
        if movie not in user_data["watched"] and movie not in friend_unique_watched:
            friend_unique_watched.append(movie) 
    return friend_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    """ 
    Finding recommended movies if:
        - user has no watched
        - at least one of user's friend watched it
        - the "host" that is in "subscriptons" field
        - return the list of recommended movies at the end 
    """
    # assign user's friend watch list that is returning from get_friends_watched_movie function
    friend_watched_list = get_friends_watched_movie(user_data)
    # list of movies that will be recommended when it matche all the conditions
    recommend_movie_list = []

    # return [] if friend watched movies is empty
    if len(friend_watched_list) == 0 or len(user_data["watched"]) == 0:
        return []

    # otherwise, find recommended movies list
    else: 
        # loop over each movie in friend watched list to check the conditions
        for movie in friend_watched_list:
            # add movie into recommended movies list without duplicating if it matches the conditions as below
            # check if user has not watched that movie and the host is in subcriptions
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:    
                # check if at least one of their friend have wathced and it is not in recommended movie list to avoid duplicated.
                if friend_watched_list.count(movie) >= 1 and movie not in recommend_movie_list:
                    recommend_movie_list.append(movie)
        return recommend_movie_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    """
    Find recommended movies if:
    - user has no watched
    - at least one of user's friend watched it
    - the "genre" is most frequent genre
    - return the list of recommended movies at the end. 
    """
    # list of recommended movies that will be return at the end
    recommend_movies_by_genre = []

    # assing most genre that is returning from get_most_watched_genre function
    most_genre = get_most_watched_genre(user_data)

    # assign user's friend watch list that is returning from get_friends_watched_movie function
    friend_watched_movies = get_friends_watched_movie(user_data)

    # return [] if friend watched movies is empty
    if len(friend_watched_movies) == 0 or len(user_data["watched"]) == 0:
        return []

    # otherwise, find recommended movies list
    else: 
        # loop over each element in friend watched movies list and compare with the conditions
        for movie in friend_watched_movies:
            
            # add movies into recommended movies list without dupliated, if it matches the conditions as below
            # check if user has no watched that moive and it is not in the recommed moive list to avoid duplicated
            if movie not in user_data["watched"] and movie not in recommend_movies_by_genre:
                # check if at least one of their friend have watched that movie and it is most frequent genre
                if friend_watched_movies.count(movie) >= 1 and movie["genre"] == most_genre:
                    # add movie into recommended movie list
                    recommend_movies_by_genre.append(movie)
        return recommend_movies_by_genre


def get_rec_from_favorites(user_data):
    """ 
    Finding recommended movies if:
    - the movie is in user's favorites
    - none of user's friend have watched it
    - return the list of recommended movies at the end. 
    """
    
    # assign user's friend watch list that is returning from get_friends_watched_movie function
    friend_watched_movies = get_friends_watched_movie(user_data)

    # list of recommended movies that will be return at the end
    recommended_from_favorites = []

    # return [] if friend watched movies is empty
    if len(friend_watched_movies) == 0 or len(user_data["watched"]) == 0:
        return []

    # otherwise, find recommended movies list from favorite
    else: 
        # loop over each movie in user's favorites list to get the movies
        for movie in user_data["favorites"]:
            # add movies into recommend list without duplicated if conditions matched
            # check if none of user's friend have wathced it and it is not in recommeded favorites list to avoid duplicated
            if movie not in friend_watched_movies and movie not in recommended_from_favorites:
                recommended_from_favorites.append(movie)
        return recommended_from_favorites