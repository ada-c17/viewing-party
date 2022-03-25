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
    # list to store all friend watched movies dictionary to compare with user wathced list
    friends_watched_movies_list = []
    
    # list of dictionary that store all movies are not in friend watched list
    unique_watched = []
    
    # create friend wathed list
    # loop to get each value of friend list
    for i in range(len(user_data["friends"])):
        
        # loop to get each value of watched list at each index of friend list
        for k in range(len(user_data["friends"][i]["watched"])):
            print()
            # each movies dictionary at each index of watched list of friend list in user data into a new list 
            # add that value, if it is not in a new list
            if user_data["friends"][i]["watched"][k] not in friends_watched_movies_list:
                friends_watched_movies_list.append(user_data["friends"][i]["watched"][k])
            
    
    # compare user watched list and friends watched list
    # loop to get each movie dictionary of user watched list and comparing with friend watched list
        
    for value in user_data["watched"]:
        
        # value variable is each movie dictionary of user watched list 
        # add value variable into a new list if it is not duplicate
        if value not in friends_watched_movies_list:
            unique_watched.append(value) 
    return unique_watched


def get_friends_unique_watched(user_data):
    # list to store all friend watched movies dictionary to compare with user wathced list
    friends_watched_movies_list = []
    
    # list of dictionary that store all movies are not in friend watched list
    friend_unique_watched = []
    
    # create friend wathed list
    # loop to get each value of friend list
    for i in range(len(user_data["friends"])):
        
        # loop to get each value of watched list at each index of friend list
        for k in range(len(user_data["friends"][i]["watched"])):
            print()
            # add each movies dictionary at each index of watched list of friend list in user data into a new list 
            # add that value, if it is not in a new list
            if user_data["friends"][i]["watched"][k] not in friends_watched_movies_list:
                friends_watched_movies_list.append(user_data["friends"][i]["watched"][k])
            
    
    # compare user watched list and friends watched list
    # loop to get each movie dictionary of firend watched movies list and comparing for comparing with user watched list  
                
    for movie in friends_watched_movies_list:
    
        # item variable is each movie dictionary of fiend watched movies list 
        # add item variable into a new list if the values is not duplicate 
        if movie not in user_data["watched"]:
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
    # list of dictionary that store all movies are friend watched list
    friend_watched_list = []
    # list of movies that will be recommended when it matche all the conditions
    recommend_movie_list = []

    # create friend wathed list
    # loop to get each value of friend list
    for i in range(len(user_data["friends"])):

        # loop to get each value of watched list at each index of friend list
        for k in range(len(user_data["friends"][i]["watched"])):
            
            # add each movies dictionary at each index of watched list of friend list in user data into a new list 
            friend_watched_list.append(user_data["friends"][i]["watched"][k])
    # add all movies that matche the condition into recommend movies list
    # loop over item in friend watched list to check the conditions
    for item in friend_watched_list:
        # add item into recommended movies list if it matches the conditions as below
        # first condition: if the item is not in user watched list
        if item not in user_data["watched"]:    
            # second condition: if the item been happened at least one time in friend watched list
            if friend_watched_list.count(item) >= 1:
                # third condition: if the key "host" of item dictionary is in subscriptions of user data 
                if item["host"] in user_data["subscriptions"]:
                    recommend_movie_list.append(item)
    return recommend_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


