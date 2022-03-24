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


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

