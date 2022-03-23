from re import T

# ------------- WAVE 1 --------------------

# This function adds 3 key-value pairs to a dictionary called movie_dict
def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

# This function adds a key-value pair called "watched" to a dictionary called user_data; It includes all movies that the user has watched 
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

# This function adds a key-value pair called "watchlist" to a dictionary called user_data. It includes all movies that the user wants to watch 
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

# This function decides whether to put a movie into a watchlist or a list of watchd movie
def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][index]["title"]:
            watched_movie = user_data["watchlist"][index]
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# This function calculates the average rating of all moviws in the watched movies
def get_watched_avg_rating(user_data):
    average_rating = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        for movie_watched in user_data["watched"]:
            average_rating += movie_watched["rating"]
        return average_rating / len(user_data["watched"])

# This function finds out the genre that is the most fewquently watched 
def get_most_watched_genre(user_data):
    # example of dict_genre_count: {'Fantasy': 3, 'Action': 1, 'Intrigue': 2}
    dict_genre_count = {}
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie_watched in user_data["watched"]:
            if movie_watched["genre"] not in dict_genre_count.keys():
                dict_genre_count[movie_watched["genre"]] = 1
            else:
                dict_genre_count[movie_watched["genre"]] += 1
        for genre, count in dict_genre_count.items():
            if count == max(dict_genre_count.values()):
                return genre


# -----------------------------------------
# ------------- Helper Function -----------
# -----------------------------------------

# Given there are three places that needs to use the movies that the user's friends have watched, this function generates a list that includes the movie that the user's friends have watched 
def generate_friends_movie_list(user_data):
    friends_movie_list_without_duplicate = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list_without_duplicate:
                friends_movie_list_without_duplicate.append(movie)
    return friends_movie_list_without_duplicate


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# This function returns a list of dictionary that represents a list of movies that the user has watched but none of their friends have watched 
def get_unique_watched(user_data):
    friends_movie_list = generate_friends_movie_list(user_data)
    user_unique_watched_list = []
    for unique_movie in user_data["watched"]:
        if unique_movie not in friends_movie_list:
            user_unique_watched_list.append(unique_movie)
    return user_unique_watched_list

# This function returns a list of dictionary that represents a list of movies that at least one of the user's friends have watched but the user has not watched 
def get_friends_unique_watched(user_data):
    friends_movie_list = generate_friends_movie_list(user_data)
    friends_unique_watched_list = []
    for unique_movie in friends_movie_list:
        if unique_movie not in user_data["watched"]:
            friends_unique_watched_list.append(unique_movie)
    return friends_unique_watched_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# This function finds a list of recommended movies based on the return value from get_friends_unique_watched(user_data) and the user's subscriptions
def get_available_recs(user_data):
    recommend_movies = []
    movies_at_least_friends_watched = get_friends_unique_watched(user_data)
    for movie in range(len(movies_at_least_friends_watched)):
        if movies_at_least_friends_watched[movie]["host"] in user_data["subscriptions"]:
            recommend_movies.append(movies_at_least_friends_watched[movie])
    return recommend_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# This function finds a list of recommended movies based on the return value from get_friends_unique_watched(user_data) and the user's most frequent genre
def get_new_rec_by_genre(user_data):
    get_new_rec_list_by_genre = []
    movies_at_least_friends_watched = get_friends_unique_watched(user_data)
    for movie in range(len(movies_at_least_friends_watched)):
        if movies_at_least_friends_watched[movie]["genre"] == get_most_watched_genre(user_data):
            get_new_rec_list_by_genre.append(movies_at_least_friends_watched[movie])
    return get_new_rec_list_by_genre

# This function finds a list of recommended movies that are in the user's favorites but none of their friends have watched 
def get_rec_from_favorites(user_data):
    friends_movie_list = generate_friends_movie_list(user_data)
    rec_to_friends_from_favorites = []
    for movie in range(len(user_data["favorites"])):
        if user_data["favorites"][movie] not in friends_movie_list:
            rec_to_friends_from_favorites.append(user_data["favorites"][movie])
    return rec_to_friends_from_favorites
