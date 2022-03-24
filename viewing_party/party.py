# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title":title,
        "genre":genre,
        "rating":rating
    }
    if title == None or genre == None or rating == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    if user_data == None or movie == None:
        return None

    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    if user_data == None or movie == None:
        return None

    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    if user_data == None or title == None or not type(title)==str :
        return None
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for item in range(len(watchlist)):
        if title == watchlist[item]["title"]:
            watched.append(watchlist[item])
            watchlist.remove(watchlist[item])
        
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    rating_list = []
    if len(watched) == 0:
        return 0.0

    for item in range(len(watched)):
        rating_list.append(float(watched[item]["rating"]))
    
    average_rating = sum(rating_list)/len(rating_list)
    return average_rating

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genre_list = []
    # occuring_count = dict()
    # count = 0

    import statistics
    from statistics import mode

    if len(watched) == 0:
        return None
    
    for item in range(len(watched)):
        genre_list.append(str(watched[item]["genre"]))

    return mode(genre_list)
    # for genre in genre_list:
    #     if genre in occuring_count:
    #         occuring_count[genre]+=1
    #     else:
    #         occuring_count[genre]=1
    # for (genre, number) in  occuring_count:


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched = user_data["watched"]
    friends = user_data["friends"]
    user_unique_watched_movies = []
    user_unique_watched_movies += watched

    if len(list(friends)) != 0 or len(watched) != 0:
        for item in friends:
            for movie in item["watched"]:
                if movie in user_unique_watched_movies:
                    user_unique_watched_movies.remove(movie)
    
    return user_unique_watched_movies


def get_friends_unique_watched(user_data):
    watched = user_data["watched"]
    friends = user_data["friends"]
    friends_unique_movies = []

    if len(list(friends)) != 0 or len(watched) != 0:
        for item in friends:
            for movie in item["watched"]:
                if movie not in watched and movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)  

    return  friends_unique_movies            
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    streaming_service = user_data["subscriptions"]
    friends_watched = user_data["friends"]
    user_watched = user_data["watched"]

    recommended_movies = []

    for item in friends_watched:
        for movie in item["watched"]:
            if movie not in user_watched and movie not in recommended_movies:
                if movie["host"] in streaming_service:
                    recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies = []
    most_watched_genre = get_most_watched_genre(user_data)
    not_watched = get_friends_unique_watched(user_data)

    for item in not_watched:
        if item["genre"] == most_watched_genre and item in not_watched:
            recommended_movies.append(item)

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    user_favorite = user_data["favorites"]
    not_watched = get_unique_watched(user_data)

    for item in not_watched:
        if item in user_favorite and item in not_watched:
            recommended_movies.append(item)

    return recommended_movies



