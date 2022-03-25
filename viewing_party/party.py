# ------------- WAVE 1 --------------------
def create_movie(movie_title, genre, rating):
    """
    create a movie profile, return movie; return None if any of the values is none
    """
    #add new movie
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating,
    }
    
    for value in new_movie.values():
        if value == None:
            return None

    return new_movie


def add_to_watched(user_data, movie):
    """
    add watched movies to "watched"
    """
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """
    add movies to watch to watchlist
    """
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    """
    moves movie from "watch list" to "watched"
    """

    copy_of_user_data = dict(user_data)
    movie_ready_to_move = {}
    for i in range(len(copy_of_user_data["watchlist"])):
        if movie_title in copy_of_user_data["watchlist"][i]["title"]:
            movie_ready_to_move = copy_of_user_data["watchlist"][i]
            user_data["watchlist"].remove(movie_ready_to_move)
            user_data["watched"].append(movie_ready_to_move)
    return user_data       

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    count average score for total rating scores in wated movie 
    """

    total_rating = 0
    average_rating = 0
    if user_data["watched"] != []:
        for movie in user_data["watched"]: 
            total_rating += movie["rating"]
        average_rating = total_rating/len(user_data["watched"])
    else:
        average_rating = 0

    return average_rating



def get_most_watched_genre(user_data):
    """
    count which movie watched most
    """

    most_watched_genre = {}
    if not user_data["watched"] == []:
        for movie in user_data["watched"]:
            if movie["genre"] not in most_watched_genre:
                most_watched_genre[movie["genre"]] = 1
            else:
                most_watched_genre[movie["genre"]] += 1

        max_value = 0
        popular_genre = ""       
        for key, value in most_watched_genre.items():
            if value >= max_value:
                max_value = value
                popular_genre = key
        return popular_genre 
    

            
# -----------------------------------------
# ------------- WAVE 3 -------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    Determine which movies the user has watched, but none of their friends have watched.
    """
    friend_watched_movie_list = []
    for dict in user_data["friends"]:
        for movie in dict["watched"]:
            friend_watched_movie_list.append(movie)

    user_unique_movies = []
    for user_movie in user_data["watched"]:
        if user_movie not in friend_watched_movie_list:
            user_unique_movies.append(user_movie)

    return user_unique_movies

    
def get_friends_unique_watched(user_data):
    """
    Determine which movies at least one of the user's friends have watched, but the user has not watched.
    """
    friend_watched_movie_list = []
    
    for dict in user_data["friends"]:
        for movie in dict["watched"]:
            if movie not in friend_watched_movie_list:
                friend_watched_movie_list.append(movie)
    
    friend_unique_watched = []      
    for friend_movie in friend_watched_movie_list:
        if friend_movie not in user_data["watched"]:
            friend_unique_watched.append(friend_movie)
    
    return friend_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """
    • Determine a list of recommended movies. A movie should be added to this list if and only if:
		○ The user has not watched it
		○ At least one of the user's friends has watched
		○ The "host" of the movie is a service that is in the user's "subscriptions"
	• Return the list of recommended movies  
    """
    
    friend_unique_watched_list = get_friends_unique_watched(user_data)
    user_subscriptions_list = user_data["subscriptions"]
    recommended_movies_list = []
    for movie in friend_unique_watched_list:
        if movie["host"] in user_subscriptions_list:
            recommended_movies_list.append(movie)
    return recommended_movies_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    • Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
		○ The user has not watched it
		○ At least one of the user's friends has watched
		○ The "genre" of the movie is the same as the user's most frequent genre
    Return the list of recommended movies
    """
    recommended_movies_by_genre = []
    most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_watched_list = get_friends_unique_watched(user_data)
    for movie in friend_unique_watched_list:
        if movie["genre"] == most_watched_genre:
            recommended_movies_by_genre.append(movie)
    return recommended_movies_by_genre


def get_rec_from_favorites(user_data):
    """
    • determine a list of recommended movies. A movie should be added to this list if and only if:
		○ The movie is in the user's "favorites"
		○ None of the user's friends have watched it
    Return the list of recommended movies
    """
    recommended_movies_to_friend_list = []
    user_unique_watched_list = get_unique_watched(user_data)
    for movie in user_unique_watched_list:
        if movie in user_data["favorites"]:
            recommended_movies_to_friend_list.append(movie)
    return recommended_movies_to_friend_list
