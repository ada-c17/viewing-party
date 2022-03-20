# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, movie):
    counter = 0
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == movie:
            user_data["watched"].append(movie_dict)
            user_data["watchlist"].pop(counter)
        counter += 1
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0.0
    average = 0.0

    for movie_dict in user_data["watched"]:
        rating_sum += movie_dict["rating"]
    
    if user_data["watched"]:
        average = rating_sum / len(user_data["watched"])
        return average
    else:
        return average

def get_most_watched_genre(user_data):
    genres = {}
    most_watched = ""
    num_watched = 0

    for movie_dict in user_data["watched"]:
        if movie_dict["genre"] in genres:
            genres[movie_dict["genre"]] += 1
        else:
            genres[movie_dict["genre"]] = 1
    
    for genre, num in genres.items():
        if num > num_watched:
            most_watched = genre
            num_watched = num
    
    if user_data["watched"]:
        return most_watched
    else:
        return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friend_list = []
    unique_list = []

    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            if movies not in friend_list:
                friend_list.append(movies)
    
    for movies in user_data["watched"]:
        if movies not in friend_list:
            unique_list.append(movies)
    
    return unique_list
        
            
def get_friends_unique_watched(user_data):
    friend_unique_list = []

    for watched_list in user_data["friends"]:
        for movies in watched_list["watched"]:
            if (movies not in user_data["watched"] and 
            movies not in friend_unique_list):
                friend_unique_list.append(movies)
    
    return friend_unique_list
   
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_list = get_friends_unique_watched(user_data)
    recs = []

    for movie in friends_list:
        if movie["host"] in user_data["subscriptions"]:
            recs.append(movie)
    
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_for_rec = get_most_watched_genre(user_data)
    genre_recs = []

    if "subscriptions" in user_data.keys():
        friend_recs = get_available_recs(user_data)
    else:
        friend_recs = get_friends_unique_watched(user_data)

    for movie in friend_recs:
        if movie["genre"] == genre_for_rec:
            genre_recs.append(movie)
    
    return genre_recs

def get_rec_from_favorites(user_data):
    faves_to_rec = []
    friend_list = []

    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            if movie not in friend_list:
                friend_list.append(movie)
    
    for movie in user_data["favorites"]:
        if movie not in friend_list:
            faves_to_rec.append(movie)

    return faves_to_rec