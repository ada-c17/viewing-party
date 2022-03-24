# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # if any of the values in our inputs are falsy 
    result = None
    

    if not title or not genre or not rating:
        return None 
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
    for key in user_data["watchlist"]:
        if key["title"] == title:
            user_data["watchlist"].remove(key)
            user_data["watched"].append(key)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

    
def get_watched_avg_rating(user_data):
    avg_rating = 0
    total_rating = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            total_rating += movie["rating"]
        avg_rating = total_rating/len(user_data["watched"])
        return avg_rating
    else:
        return 0.0

def get_most_watched_genre(user_data):
    popular_genre = None
    count = {}
    frequent_count = 0
    for movie in user_data["watched"]: 
        if movie["genre"] not in count:
            count[movie["genre"]] = 0
        count[movie["genre"]] =+ 1
    
    for genre in count:
        if count[genre] > frequent_count:
            frequent_count = count[genre]
            popular_genre = genre
    return popular_genre 
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # print(user_data)
    list_of_dicts = []
    friends_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_list.append(movie)
            # print(friends_list)

    for movie in user_data["watched"]:
        if movie not in friends_list:
            list_of_dicts.append(movie)
    return list_of_dicts


def get_friend_watched(user_data):
    friends_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_list.append(movie)
    return friends_list
    
def get_friends_unique_watched(user_data):
    list_of_movies = []
    for movie in get_friend_watched(user_data):
        if movie not in user_data["watched"]\
            and movie not in list_of_movies:
                list_of_movies.append(movie)    
    return list_of_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    reccomendations = []
    for movie in get_friends_unique_watched(user_data):
        # print(movie)
        if movie["host"] in user_data["subscriptions"]:
            reccomendations.append(movie)
    return reccomendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    ultimate_reccs = []
    top_genre = get_most_watched_genre(user_data)

    
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == top_genre:
            ultimate_reccs.append(movie)
    return ultimate_reccs


def get_rec_from_favorites(user_data):
    fave_reccs = []
    user_watched = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in user_watched:
            fave_reccs.append(movie)
        

    return fave_reccs