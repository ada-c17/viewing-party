# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title   
        movie_dict["genre"] = genre        
        movie_dict["rating"] = rating
    else: 
        return None    
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watched"].append(item)
            user_data["watchlist"].remove(item)
    return user_data
        # else:
        #    return user_data    

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    rating_sum = 0.0
    
    if len(user_data["watched"]) > 0:
        for movie in range(len(user_data["watched"])):
            rating_sum += user_data["watched"][movie]["rating"]  
        average_rating = rating_sum / len(user_data["watched"])
    return average_rating 

def get_most_watched_genre(user_data):
    genre_dict = {}
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in range(len(user_data["watched"])):
            if user_data["watched"][movie]["genre"] in genre_dict:
                genre_dict[user_data["watched"][movie]["genre"]] += 1
            else:
                genre_dict[user_data["watched"][movie]["genre"]] = 0
    most_watched = max(genre_dict, key=genre_dict.get)            
    return most_watched                  
# -----------------------------------------


# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    unique_movie_list = []
    combined_friend_movie_list = []

    for friend_index in range(len(user_data["friends"])):
        user_friend_index = user_data["friends"][friend_index]["watched"]
        for film in range(len(user_friend_index)):
            combined_friend_movie_list.append(user_friend_index[film])
    for movie in range(len(user_data["watched"])):
        user_watched_title = user_data["watched"][movie]
        if user_watched_title not in combined_friend_movie_list and\
            user_watched_title not in unique_movie_list:
            unique_movie_list.append(user_watched_title)
    return unique_movie_list

def get_friends_unique_watched(user_data):
    combined_friend_movie_list_no_dups = []
    unique_friend_movie_list = []

    for friend_index in range(len(user_data["friends"])):
        user_friend_index = user_data["friends"][friend_index]["watched"]
        for film in range(len(user_friend_index)):
            if user_friend_index[film] not in combined_friend_movie_list_no_dups:
                combined_friend_movie_list_no_dups.append(user_friend_index[film])

    for movie in combined_friend_movie_list_no_dups:
        if movie not in user_data["watched"] and\
            movie not in unique_friend_movie_list:
            unique_friend_movie_list.append(movie)
    return unique_friend_movie_list                    
# -----------------------------------------


# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    movie_recs = []
    unique_friend_movie_list = get_friends_unique_watched(user_data)

    for friend_movie in unique_friend_movie_list:
        if friend_movie["host"] in user_data["subscriptions"] and\
            friend_movie not in user_data["watched"]:
            movie_recs.append(friend_movie)
    return movie_recs
# -----------------------------------------

# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    # consider user's most frequently watched genre
    # determine list of recc'd movies
    # movie should be added to list ONLY if:
    # - movie not in user_data["watched"]
    # - at least one of user's friends have watched
    # - ["genre"] of movie is the same as user's most frequent genre
    movie_rec_list = []
    available_rec_list = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    for movie_rec in available_rec_list:
        if movie_rec["genre"] == most_watched_genre:
            movie_rec_list.append(movie_rec)

    return movie_rec_list

def get_rec_from_favorites():
    pass
# -----------------------------------------

