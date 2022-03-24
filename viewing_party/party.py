# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass
    # using the parameters title, genre, and rating, create a dictionary called new_movie
    # with keys "title", "genre", and "rating"
    # and values that are equal to title, genre, rating

    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        new_movie = None

    return new_movie

def add_to_watched(user_data, movie):
    # this function should add the dictionary movie to user_data.
    # user_data is also a dictionary with one key, "watched"
    # the value of user_data["watched"] is a list of dictionaries (i.e., each movie),
    # each with keys "title", "genre", and "rating"

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    # this function will loop through the list user_data["watchlist"]
    # if user_data["watch_ist"][i]["title"] == movie_title, 
    # that inner dictionary will be added to user_data["watched"]
    # and be removed from user_data["watchlist"]

    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # this function accesses the ratings for all of the movies in watched
    # and returns the average of those ratings

    total = 0

    for movie in user_data["watched"]:
        # add each movie's rating to the total
        total += movie["rating"]
    
    # calculate average rating for all movies within "watched"
    if total == 0:
        rating_average = 0
    else:
        rating_average = total/len(user_data["watched"])

    return rating_average

def get_most_watched_genre(user_data):
    # create an empty dictionary called movie_genre_count
    # within user_data["watched"], iterate through each movie and access user_data["watched"][movie]["genre"]
    # if the genre isn't in movie_genre_count, set movie_genre_count[genre] = 1
    # otherwise, set movie_genre_count[genre] += 1
    # set popular_genre = max value from movie_genre_count
    # return popular_genre
    
    # empty dictionary to hold movie genres and their frequency
    movie_genre_count = {}

    # check if watched list is empty
    if not user_data["watched"]:
        popular_genre = None
    else:
        # loop to update movie_genre_count based on watch history
        for movie in user_data["watched"]:
            genre = movie["genre"]
            if genre not in movie_genre_count:
                movie_genre_count[genre] = 1
            else:
                movie_genre_count[genre] += 1

        # convert movie_genre_count keys and values to lists to allow for max function
        key_list = list(movie_genre_count.keys())
        value_list = list(movie_genre_count.values())
        max_value = max(value_list)

        # identify index of most popular genre
        popular_genre_index = value_list.index(max_value)

        # identify the most frequently watched movie genre
        popular_genre = key_list[popular_genre_index]

    return popular_genre




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # create an empty list called movies_in_common and my_unique_movies
    # loop through user_data["friends"]. for friend in user_data["friends"],
    # for movie in user_data["friends"][friend]["watched"],
    # if movie in user_data["watched"], movies_in_common.append(movie)
    # loop through user_data["watched"] and compare to movies_in_common list
    # if the movie is not in movies_in_common, add it to my_unique_movies
    # return my_unique_movies

    # create lists to store unique movies and movies that user and friends have watched
    movies_in_common = []
    my_unique_movies = []

    # loop through friends' watched movies to identify movies user and friends have both watched
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            if movie in user_data["watched"]:
                movies_in_common.append(movie)
    
    # loop through user's watched movies and compare to movies in common to find unique movies
    for my_movie in user_data["watched"]:
        if my_movie not in movies_in_common:
            my_unique_movies.append(my_movie)
    
    return my_unique_movies

def get_friends_unique_watched(user_data):

    # list to store movies only friends have watched
    friends_unique_movies = []

    # loop through friends' watched movies to identify movies that friends have watched, but user hasn't watched
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    # empty list to hold movie recommendations
    my_recommended_movies = []

    # loop through all of the movies that the user's friends have watched
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            # check that the user hasn't watched the movie, the user has the movie's correct subscription service, and the movie isn't already recommended
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"] and movie not in my_recommended_movies:
                my_recommended_movies.append(movie)
    
    return my_recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    # list to store recommended movies in user's most popular genre
    my_recs_by_genre = []
    
    # variable to identify user's most watched genre using helper function
    most_popular_genre = get_most_watched_genre(user_data)

    # variable to identify movies that the user hasn't watched, but their friends have watched
    unwatched_friends_movies = get_friends_unique_watched(user_data)

    # check list of unwatched movies that friends have watched; add any that are user's most-watched genre to recs list
    for movie in unwatched_friends_movies:
        if movie["genre"] == most_popular_genre:
            my_recs_by_genre.append(movie)
    
    return my_recs_by_genre