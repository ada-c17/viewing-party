# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    ### refactoring post-submission
    # OG code:
    # new_movie = {}
    # if title == None:
    #     return None
    # elif genre == None:
    #     return None
    # elif rating == None:
    #     return None
    # else:
    #     new_movie["title"] = title
    #     new_movie["genre"] = genre
    #     new_movie["rating"] = rating

    ### more pythonic to use not, and condense checks onto one line
    if not (title and genre and rating):
        return None
    ### create new dictionary after checking that we have valid input, wastes less memory
    else:
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    movie_index = -1

    # find index of watched movie in watchlist list
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            movie_index = i

    # if movie is found to be in watchlist
    if movie_index >= 0:
        # remove element at that index from watchlist list and add to variable
        watched_movie = user_data["watchlist"].pop(movie_index)

        # add variable to watched list
        user_data["watched"].append(watched_movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """
    Returns user's average movie rating.
    """
    ### refactoring post-submission
    # OG code:
    # sum = 0
    # average = 0
    # watched_list_length = len(user_data["watched"])

    # if watched_list_length > 0:
    #     # total up ratings
    #     for i in range(watched_list_length):
    #         sum += user_data["watched"][i]["rating"]
    #     # divide total by number of movies to get average
    #     average = sum / watched_list_length
    # return average

    ### refactored version:
    ### more pythonic to use truthy/falsy
    if user_data["watched"]:
        ### declaring variables after checking if valid input saves memory
        sum = 0
        average = 0
        
        ### simplify syntax by using movie instead of i
        for movie in user_data["watched"]:
            sum += movie["rating"]
        average = sum / len(user_data["watched"])
        return average
    else:
        return 0

def get_most_watched_genre(user_data):
    """
    Returns user's most watched genre.
    """
    ### refactoring post-submission:
    # OG code:
    # if len(user_data["watched"]) > 0:
    #     # make new list for just genres, with repetitions
    #     watched_genre_list = []
    #     for i in range(len(user_data["watched"])):
    #         watched_genre_list.append(user_data["watched"][i]["genre"])

    ### refactored version:
    if user_data["watched"]:
        watched_genre_list = []
        for movie in user_data["watched"]:
            watched_genre_list.append(movie["genre"])
        
        # OG code resumes:
        most_watched_count = 0
        most_watched_genre = ''

        # iterate through genre list, counting how many times each genre appears
        for genre in watched_genre_list:
            genre_count = watched_genre_list.count(genre)
            # update most_watched_genre and genre count with whatever comes back highest
            if genre_count > most_watched_count:
                most_watched_count = genre_count
                most_watched_genre = genre
        ### refactoring possibility:
        ### use max function with list.count as key
        ### most_watched_genre = max(watched_genre_list, key = watched_genre_list.count)


        return most_watched_genre
    else:
        return None
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    """
    Creates list of movies that user has watched but friends haven't.

    Parameters: user data, including user's watched list, and friends watched lists

    Returns: new list of movie information dictionaries
    """
    # # create empty list to store unique movies
    # user_unique_watched = []

    # # iterate over user's watched list
    # for i in range(len(user_data["watched"])):
    #     # set flag to signal if we're still looking
    #     searching_for_movie = True

    #     # set current title we're looking for
    #     looking_for_title = user_data["watched"][i]["title"]

    #     while searching_for_movie:
    #         # iterate through friends list
    #         for friend in user_data["friends"]:
    #             friend_index = user_data["friends"].index(friend)
    #             # iterate through every movie on friend's watch list
    #             if searching_for_movie:
    #                 for num in range(len(user_data["friends"][friend_index]["watched"])):
    #                     # if title matches title we're looking for, break out of loop and start looking for next title
    #                     # once a title has been found once, we don't need to see if it's been watched by multiple friends
    #                     if user_data["friends"][friend_index]["watched"][num]["title"] == looking_for_title:
    #                         searching_for_movie = False
    #                         break
    #                     else:
    #                         continue
    #             # if no longer searching for movie, break out of loops until searching movie is changed
    #             elif not searching_for_movie:
    #                 break
    #         # if after iterating through all friends watched lists we are still looking, add movie to the unique list
    #         if searching_for_movie:
    #             user_unique_watched.append(user_data["watched"][i])
    #             # then change flag to switch to next movie
    #             searching_for_movie = False
    #     # continue until all movies on user's watch list have been checked. 
    #     continue

    # return user_unique_watched       

    ### refactoring possibility 1
    # friend_movies = []
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie not in friend_movies:
    #             friend_movies.append(movie)
    
    # user_unique_watched = []
    # for movie in user_data["watched"]:
    #     if movie not in friend_movies:
    #         user_unique_watched.append(movie)
    
    # return user_unique_watched

    ### refactoring using sets!!!
    friend_movies_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            friend_movies_set.add(title)

    user_movies_set = set()
    for movie in user_data["watched"]:
        user_movies_set.add(movie["title"])
    
    unique_titles = user_movies_set - friend_movies_set
    
    user_unique_watched = []

    for movie in user_data["watched"]:
        if movie["title"] in unique_titles:
            user_unique_watched.append(movie)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    """
    Creates list of movies that user's friends have watched that user hasn't.

    Parameters: user's data, including users's watched list and friends' watched lists

    Returns: new list of movie information dictionaries
    
    """
    # refactoring post-submission:
    # OG Code:
    # friends_unique_watched = []

    # friends_unique_watched_titles = []
    
    # # iterate through friends list
    # for friend in user_data["friends"]:
    #     friend_index = user_data["friends"].index(friend)
    #     # iterate through specific friend's watched list
    #     for i in range(len(user_data["friends"][friend_index]["watched"])):
    #         # set title we're currently considering
    #         looking_for_title = user_data["friends"][friend_index]["watched"][i]["title"]

    #         searching_for_movie = True
    #         # start iterating over user's watched list
    #         for num in range(len(user_data["watched"])):
    #             # check if title matches item on user's watched list, leave loop if so
    #             if looking_for_title == user_data["watched"][num]["title"]:
    #                 searching_for_movie = False
    #                 break
    #         # start looking for next movie
    #         if not searching_for_movie:
    #             continue
    #         # if movie not on user's watched list, see if it is already on unique_watched_list
    #         elif looking_for_title in friends_unique_watched_titles:
    #             continue
    #         # if movie not on user's watched list and not on unique_watched_list, add it
    #         else:
    #             friends_unique_watched_titles.append(looking_for_title)
    #             friends_unique_watched.append(user_data["friends"][friend_index]["watched"][i])
    
    # return friends_unique_watched

    ### refactoring possibility 1
    # user_watched_list = []
    # for movie in user_data["watched"]:
    #     user_watched_list.append(movie)
    
    # friends_unique_watched = []
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie not in user_watched_list and movie not in friends_unique_watched:
    #             friends_unique_watched.append(movie)
    
    # return friends_unique_watched

    ### refactoring with sets!

    user_movies_set = set()
    for movie in user_data["watched"]:
        user_movies_set.add(movie["title"])
    
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_movies_set and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    
    return friends_unique_watched




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """
    Creates list of recommended movies based on user's friends watched lists and user subscriptions

    Parameters: user data, including user's watched lists, friends' watched lists, and user subscription info

    Returns: new list of movie dictionaries
    """

    available_recs = []

    friends_watched = get_friends_unique_watched(user_data)

    # OG code:
    # check friends unique watched list hosts against user subscriptions
    # for i in range(len(friends_watched)):
    #     if friends_watched[i]["host"] in user_data["subscriptions"]:
    #         available_recs.append(friends_watched[i])

    ### refactoring possibility:
    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    
    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    Creates list of recommended movies based on user's favorite genre

    Parameters: user data, including user and friends' watched lists

    Returns: new list of movie dictionaries
    """
    genre_rec_list = []

    # determine user's most watched genre
    most_watched_genre = get_most_watched_genre(user_data)

    # get list of movies friends have watched that user hasn't
    friends_recommend = get_friends_unique_watched(user_data)

    for movie in friends_recommend:
        # refactoring post-submission:
        # OG code:
        # if friends_recommend[friends_recommend.index(movie)]["genre"] == most_watched_genre:

        ### refactored version:
        if movie["genre"] == most_watched_genre:
            genre_rec_list.append(movie)
    
    return genre_rec_list

def get_rec_from_favorites(user_data):
    """
    Creates list of user's favorite movies that user's friends have not watched

    Parameters: user data, including favorites list and friends' watched lists

    Returns: new list of movie dictionaries
    """
    favorites_rec_list = []

    unique_watchlist = get_unique_watched(user_data)
    # compare movies in user's unique watchlist to user favorites
    for movie in unique_watchlist:
        if movie in user_data["favorites"]:
            favorites_rec_list.append(movie)
    
    return favorites_rec_list
