# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    new_movie = {}

    # check that all necessary movie characteristics exist before creating new movie
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        new_movie = None

    return new_movie

def add_to_watched(user_data, movie):

    # add movie to watched list
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    # add movie to watchlist
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):

    # move movies that user watches from watchlist to watched
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    # variable to hold sum of all movie ratings
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
    
    # empty dictionary to hold movie genres and their frequency
    movie_genre_count = {}

    # check if watched list is empty; if so, there will be no most watched genre
    if not user_data["watched"]:
        popular_genre = None
    else:
        # update movie_genre_count based on watch history
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
    
    # list to store recommended movies in user's most watched genre
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

def get_rec_from_favorites(user_data):

    # list to hold recommended movies
    my_recs_from_favorites = []

    # variable to identify movies that user's friends have not watched
    # note for future refactoring: consider updating to include movies from user's watchlist that friends haven't watched
    my_watched_movies = get_unique_watched(user_data)

    # add any movies that are in the watched list and favorites list to recommendations
    for movie in my_watched_movies:
        if movie in user_data["favorites"]:
            my_recs_from_favorites.append(movie)

    return my_recs_from_favorites
