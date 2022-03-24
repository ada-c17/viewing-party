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
        for i in range(len(user_data["watched"])):
            # sum all rating of user data watched list
            sum_rating += user_data["watched"][i]["rating"]
        # calculate the average rating
        average_rating = sum_rating / len(user_data["watched"])
    return average_rating


def get_most_watched_genre(user_data):
    """ finding most watched genre and return it """

    # return 0, if the user data watched is empty
    if len(user_data["watched"]) == 0:
        return None

    # otherwise, finding most watched genre
    else:
        # This dictionary has key is value of genre from user watched, value is numbers of duplication of genre
        genre = {}
        # variable to find most watched genre
        max_value = 0
        # variable to store most watched genre and return at the end
        most_watched_genre = ""

        # create a dictionary that has key is value of genre and value is numbers of duplication of genre from user watched
        # loop over each element of user watched to genre
        for item in user_data["watched"]:
            # assigne genre to key variable
            key = item["genre"]

            # add key as key of genre dictionary and assigne 0 as value 
            if key not in genre:
                genre[key] = 0
            # increasing by 1 if genre of user watched is in genre dictionary 
            if item["genre"] in genre:
                genre[key] += 1
        
        # find most watched genre
        # loop over key and value of genre dictionary to use on purpose finding most watched genre
        for key, value in genre.items():
            # if value value greater than max_value 
            # assign  value to max_value for comparing next value
            # assign key of dictionary to most_watched_genre that is the answer after finishing comparing
            if value > max_value:
                max_value = value
                most_watched_genre = key
        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


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


        

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


