# # ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating

    return movie_dict

def add_to_watched(user_data, movie):
    new_movie = create_movie(movie["title"],movie["genre"],movie["rating"])
    user_data["watched"] = [new_movie]

    return user_data

def add_to_watchlist(user_data, movie):
    new_movie = create_movie(movie["title"],movie["genre"],movie["rating"])
    user_data["watchlist"] = [new_movie]

    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:      
            movie = user_data["watchlist"][i]
            user_data["watched"].append(movie)
            del user_data["watchlist"][i]

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_of_ratings = 0.0
    ratings_avg = 0.0
    length = len(user_data["watched"])
    if length > 0:
        for i in range(length):
            sum_of_ratings += user_data["watched"][i]["rating"]      
            
        ratings_avg = sum_of_ratings/length

        return ratings_avg
    else:
        return 0.0
    
def get_most_watched_genre(user_data):
    count_dict = {}
    cntr = 0
    next_genre = ""
    length = len(user_data["watched"])

    if length > 0:
        for i in range(length):
            next_genre += user_data["watched"][i]["genre"] 
        
            if next_genre in count_dict:
                cntr += 1
            else:
                cntr = 1
            
            count_dict.update({next_genre:cntr})    
        
        max_value = max(count_dict, key=count_dict.get)

        return max_value
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched_len = len(user_data["watched"])   
    friends_len = len(user_data["friends"]) 
    watched_title = ""
    friends_title = ""
    unique_movie = ""
    unique_movies = []
    friends_movie_titles = []

    for i in range(friends_len):
        friends_movie_num = len(user_data["friends"][i]["watched"])
        cntr = 0
        while cntr < friends_movie_num:
            friends_title = user_data["friends"][i]["watched"][cntr]["title"]
            friends_movie_titles.append(friends_title)
            cntr += 1

    for j in range(watched_len):
        watched_title = user_data["watched"][j]["title"]
            
        if watched_title in friends_movie_titles:
            continue
        else:
            unique_movie = user_data["watched"][j]
            unique_movies.append(unique_movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    watched_len = len(user_data["watched"])   
    friends_len = len(user_data["friends"]) 
    friends_title = ""
    user_title = ""
    unique_movie = ""
    unique_movies = []
    users_movie_titles = []

    for i in range(watched_len):
        user_title = user_data["watched"][i]["title"]
        users_movie_titles.append(user_title)

    for j in range(friends_len):
        friends_movie_num = len(user_data["friends"][j]["watched"])
        cntr = 0
        while cntr < friends_movie_num:
            friends_title = user_data["friends"][j]["watched"][cntr]["title"]
            cntr += 1

            if friends_title in users_movie_titles:
                continue
            else:
                unique_movie = user_data["friends"][j]["watched"][cntr - 1]
                if unique_movie in unique_movies:
                    continue
                else:
                    unique_movies.append(unique_movie)
            
    return unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    watched_len = len(user_data["watched"])   
    friends_len = len(user_data["friends"]) 
    friends_title = ""
    user_subs = []
    friends_host = ""
    user_title = ""
    friend_rec = ""
    friend_recs = []
    user_movie_titles = []

    for i in range(watched_len):
        user_title = user_data["watched"][i]["title"]
        user_movie_titles.append(user_title)

    for j in range(friends_len):
        friends_movie_num = len(user_data["friends"][j]["watched"])
        user_subs = user_data["subscriptions"]

        cntr = 0
        while cntr < friends_movie_num:
            friends_title = user_data["friends"][j]["watched"][cntr]["title"]
            friends_host = user_data["friends"][j]["watched"][cntr]["host"]
            
            cntr += 1

            if friends_title in user_movie_titles or friends_host not in user_subs:
                continue
            else:
                friend_rec = user_data["friends"][j]["watched"][cntr - 1]
                if friend_rec in friend_recs:
                    continue
                else:
                    friend_recs.append(friend_rec)

    return friend_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    movie_genre = ""
    movie_recs = []  

    top_genre = get_most_watched_genre(user_data)
    
    friends_unique = get_friends_unique_watched(user_data)

    length = len(friends_unique)

    for i in range(length):
        movie_genre = friends_unique[i]["genre"]
        if movie_genre == top_genre:
            movie_recs.append(friends_unique[i])

    return movie_recs

def get_rec_from_favorites(user_data):
    favorites = []
    user_movie_recs = []

    favorites = user_data["favorites"]
    
    for favorite in favorites:
        user_unique = get_unique_watched(user_data)
        if favorite in user_unique:
            user_movie_recs.append(favorite)

    return user_movie_recs