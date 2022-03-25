import statistics
# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(title, genre, rating):
    # create movie information
    movie_info = {}
    if title == None or genre == None or rating == None:
        return None
    movie_info['title'] = title
    movie_info['genre'] = genre
    movie_info['rating'] = rating
    return movie_info 


def add_to_watched(user_data, movie):
    # add movie to what user has watched
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    # add movie to user's watchlist
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    # add a watched movie to watched
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
    # remove watched movie from watchlist
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    combined_rating = 0
    if user_data["watched"] == []:
        average = 0.0
    # calculate average of rating
    for movie in user_data["watched"]:
        combined_rating += movie["rating"]
        average = (combined_rating/len(user_data["watched"]))
    return average


def get_most_watched_genre(user_data):
    # make a list to store genre
    mode_list = []
    if len(user_data["watched"]) == 0:
        return None
    # use mode function to find genre mode of mode list
    for movie in user_data["watched"]:
        mode_list.append(movie["genre"])
    return statistics.mode(mode_list)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # make list of friends movies
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie["title"])
    user_unique_movies = []
    # if movie is not in friends movie list, add to user unique movies
    for movie in user_data["watched"]:
        if movie["title"] not in friend_movies:
            user_unique_movies.append(movie)
    return user_unique_movies


def get_friends_unique_watched(user_data):
    # make list of user movies
    user_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie["title"])
    # if movie not in users movie list, add to friend unique movies
    friend_unique_movies = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_movies:
                friend_unique_movies[movie["title"]] = movie
    friend_unique = list(friend_unique_movies.values())
    return friend_unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # use helper function to get friends unique movies
    friend_unique_movies = get_friends_unique_watched(user_data)
    # iterate through friends unique movies and add movie to list if host is in user's subscriptions
    recommended_movies = []
    for movie in friend_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    user_most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_movies = get_friends_unique_watched(user_data)
    user_recommended_movies = []
    for movie in friend_unique_movies:
        if movie["genre"] == user_most_watched_genre:
            user_recommended_movies.append(movie)
    return user_recommended_movies


def get_rec_from_favorites(user_data):
    # use helper function to get user unique movies
    user_unique_movies = get_unique_watched(user_data)
    # create list with favorite movies
    favorite_movies = []
    for movie in user_data["favorites"]:
        favorite_movies.append(movie)
    # iterate over favorite movies and check if has not been watched by friends
    movie_from_favorites = []
    for movie in favorite_movies:
        if movie in user_unique_movies:
            movie_from_favorites.append(movie)
    return movie_from_favorites