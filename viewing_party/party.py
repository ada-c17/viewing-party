# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {"title": title,
    "genre": genre,
    "rating": rating
    }

    for value in new_movie.values():
        if value == None:
            return None

    return new_movie


def add_to_watched(user_data_dict, movie_dict):
    updated_data = user_data_dict
    movie_list = []
    movie_list.append(movie_dict)

    updated_data["watched"] = movie_list

    return updated_data


def add_to_watchlist(user_data, movie):
    updated_watchlist = user_data
    movie_list = []
    movie_list.append(movie)

    updated_watchlist["watchlist"] = movie_list

    return updated_watchlist


def watch_movie(user_data, movie_title):
    user_data_dict = user_data

    for movie in user_data_dict["watchlist"]:
        if movie_title in movie.values():
            user_data_dict["watched"].append(movie)
            user_data_dict["watchlist"].remove(movie)
    
    return user_data_dict


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    rating_sum = 0

    watched_movies_list = user_data["watched"]

    if watched_movies_list:
        for movie in watched_movies_list:
            rating_sum += movie["rating"]
        return rating_sum / len(watched_movies_list)
    else:
        return 0


def get_most_watched_genre(user_data):
    
    watched_movies_list = user_data["watched"]
    genres_list = []
    watched_by_genre = {}

    #creates a list of genres watched, with duplicates
    if watched_movies_list:
        for movie in watched_movies_list:
            genres_list.append(movie["genre"])
    else:
        return None
    
    #dictionary with genres as keys and amount of movies of that genre watched as values by counting times genre is in genres_watched list
    for genre in genres_list:
        watched_by_genre[genre] = genres_list.count(genre)
    
    top_times_watched = 0
    top_genre = None
    
    # looping through dictionary to find most popular genre
    for genre in watched_by_genre:
        times_watched = watched_by_genre[genre]
        if times_watched > top_times_watched:
            top_times_watched = times_watched
            top_genre = genre
    
    return top_genre
    




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    
    friends_watched_movies = set()
    user_watched_movies = set()

    # creates a set of friends' watched movies
    for friend in user_data["friends"]:
        for watched_list in friend["watched"]:
            friends_watched_movies.add(watched_list['title'])
    
    # creates a set of user's watched movies
    for movie in user_data["watched"]:
        user_watched_movies.add(movie["title"])

    unique_movie_titles = (user_watched_movies - friends_watched_movies)

    unique_movies_data = []

    #looks for unique movies in user_data and adds movie data dictionary to unique_movies_data. this could be turned into a helper function
    for movie in unique_movie_titles:
        for i in range(len(user_data["watched"])):
            if movie == user_data["watched"][i]["title"]:
                unique_movies_data.append(user_data["watched"][i])

    return unique_movies_data


def get_friends_unique_watched(user_data):
    friends_watched_movies = set()
    user_watched_movies = set()
    
    for friend in user_data["friends"]:
        for watched_list in friend["watched"]:
            friends_watched_movies.add(watched_list['title'])

    for movie in user_data["watched"]:
        user_watched_movies.add(movie["title"])

    unique_movie_titles = (friends_watched_movies - user_watched_movies)

    unique_movies_data = []

    for movie in unique_movie_titles:
        for friend in (user_data["friends"]):
            for i in range(len(friend["watched"])):
                if movie == friend["watched"][i]["title"] and friend["watched"][i] not in unique_movies_data:
                    unique_movies_data.append(friend["watched"][i])

    return unique_movies_data



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_recs = []
    user_subscriptions = user_data["subscriptions"]

    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            if movie["host"] in user_subscriptions and movie not in user_data["watched"]:
                available_recs.append(movie)
    
    return available_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs = []

    if user_data["watched"] and user_data["friends"][0]["watched"]: #should probably check more than just index 0
        favorite_genre = get_most_watched_genre(user_data)
        all_recs = get_available_recs(user_data)

        for rec in all_recs:
            if rec["genre"] == favorite_genre:
                recs.append(rec)

    return recs

def get_rec_from_favorites(user_data):
    recs = []

    unique_watched = get_unique_watched(user_data)

    for movie in unique_watched:
        if movie in user_data["favorites"]:
            recs.append(movie)

    return recs