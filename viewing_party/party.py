# ------------- WAVE 1 --------------------
#this is where I will create a function
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    movie_dictionary ={}
    movie_dictionary["title"] = title
    movie_dictionary["genre"] = genre
    movie_dictionary["rating"] = rating

    return movie_dictionary

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watchlist"].remove(item)
            user_data["watched"].append(item)
    return user_data
        


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    list_of_ratings=[]
    for item in user_data["watched"]:
        list_of_ratings.append(item["rating"])
    if len(list_of_ratings) == 0:
        list_of_ratings.append(0)
    return sum(list_of_ratings)/len(list_of_ratings)

def get_most_watched_genre(user_data):
    list_of_genres=[]
    for item in user_data["watched"]:
        list_of_genres.append(item["genre"])
    if len(list_of_genres) == 0:
        return None
    popular_value = max(set(list_of_genres), key = list_of_genres.count) #getting the mode of a list
    return popular_value

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    list_both_watched = []
    for i in range(len(user_data["watched"])):
        for j in range(len(user_data["friends"])):
            for k in range(len(user_data["friends"][j]["watched"])):
                if user_data["watched"][i]["title"] == user_data["friends"][j]["watched"][k]["title"] \
                    and user_data["watched"][i]["title"] not in list_both_watched:
                    list_both_watched.append(user_data["watched"][i])
    
    list_user_watched = []
    for i in range(len(user_data["watched"])):
        list_user_watched.append(user_data["watched"][i])

    list_unique_watched = []
    for item in list_user_watched:
        if item not in list_both_watched:
            list_unique_watched.append(item)

    return list_unique_watched

def get_friends_unique_watched(user_data):
    list_both_watched = []
    for i in range(len(user_data["watched"])):
        for j in range(len(user_data["friends"])):
            for k in range(len(user_data["friends"][j]["watched"])):
                if user_data["watched"][i]["title"] == user_data["friends"][j]["watched"][k]["title"] \
                    and user_data["watched"][i]["title"] not in list_both_watched:
                    list_both_watched.append(user_data["watched"][i])
    
    list_friend_watched = []
    for j in range(len(user_data["friends"])):
            for k in range(len(user_data["friends"][j]["watched"])):
                list_friend_watched.append(user_data["friends"][j]["watched"][k])

    list_unique_friend_watched = []
    for item in list_friend_watched:
        if item not in list_both_watched and item not in list_unique_friend_watched:
            list_unique_friend_watched.append(item)

    return list_unique_friend_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friend_recs = get_friends_unique_watched(user_data)
    for item in friend_recs:
        if item["host"] in user_data["subscriptions"]:
            recommended_movies.append(item)
    return recommended_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

