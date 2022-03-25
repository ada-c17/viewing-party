# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None

    new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            movie_watched = user_data["watchlist"][i]
            del user_data["watchlist"][i]
            user_data["watched"].append(movie_watched)  
    return user_data

    # .haskey() does NOT work in python3 --> use key in list of dictionary

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0
    count = 0
    for i in range(len(user_data["watched"])):
        sum_rating += user_data["watched"][i]["rating"]
        count += 1
    if count == 0:
        return 0
    else:
        return sum_rating/count

def get_most_watched_genre(user_data):
    genre_list = []
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"])
    if len(genre_list) == 0:
        return None
    else:
        # To get the most frequent genre. I'm not sure if it accounts for ties.
        return max(set(genre_list), key=genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # make friends_movie_list 
    friends_movie_list = []
    for dictionary in user_data["friends"]:
        for movie in dictionary["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)
    # alternative way: friends_movie_lists = [d["watched"] for d in user_data["friends"]] 

    # iterate over user_data["watched"] and add each unique movie to a new empty list
    unique_watched_list = []
    
    for movie in user_data["watched"]:
        if movie not in friends_movie_list and movie not in unique_watched_list:
            unique_watched_list.append(movie)

    # return unique_watched_list
    return unique_watched_list      

def get_friends_unique_watched(user_data):
    # make friends_movie_list 
    friends_movie_list = []
    for dictionary in user_data["friends"]:
        for movie in dictionary["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)
    # alternative method: friends_movie_lists = [d["watched"] for d in user_data["friends"]]
    #                     flat_list = [movie for sublist in friends_movie_lists for movie in sublist]
    

    # iterate over friends_movie_list and add each unique movie into a new empty list.
    friends_unique_list = []
    for movie in friends_movie_list:
        if movie not in user_data["watched"] and movie not in friends_unique_list:
            friends_unique_list.append(movie)
    return friends_unique_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # get friends_unique_watched_list
    friends_unique_list = get_friends_unique_watched(user_data)
    # iterate over friends unique list and see if each movie["host"] value \
    # in user's subscription hosts
    # if so, add to a recommended list
    recommended_list = []
    for movie in friends_unique_list:
        if movie["host"] in user_data["subscriptions"]:
            recommended_list.append(movie)
    return recommended_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friends_unique_list = get_friends_unique_watched(user_data)
    genre_list = []
    new_rec = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    if len(genre_list) > 0:  
        max_genre = max(set(genre_list), key=genre_list.count) 
        for movie in friends_unique_list:
            if movie["genre"] == max_genre:
                new_rec.append(movie)
    return new_rec


def get_rec_from_favorites(user_data):
    user_unique_list = get_unique_watched(user_data)
    fav_recs = []
    for movie in user_unique_list:
        if movie in user_data["favorites"]:
            fav_recs.append(movie)
    return fav_recs

