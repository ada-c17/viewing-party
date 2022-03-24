# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    movie ={}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

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
    # Not using list comprehension
    # list_of_ratings=[]
    # for item in user_data["watched"]:
    #     list_of_ratings.append(item["rating"])
    
    # Using list comprehension
    list_of_ratings = [item["rating"] for item in user_data["watched"]]

    # This will account for the situation when the watched list is empty
    if len(list_of_ratings) == 0:
        list_of_ratings.append(0)
    
    return sum(list_of_ratings)/len(list_of_ratings)

def get_most_watched_genre(user_data):
    # Not using list comprehension
    # list_of_genres = []
    # for item in user_data["watched"]:
    #     list_of_genres.append(item["genre"])
    
    # Using list comprehension
    list_of_genres = [item["genre"] for item in user_data["watched"]]

    # This will account for the situation when the watched list is empty
    if len(list_of_genres) == 0:
        return None
    
    # Getting the mode of the list of genres
    popular_genre = max(set(list_of_genres), key = list_of_genres.count)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # Method that doesn't use list comprehension, and would work if a friend gave a move a different rating than the user 
    # list_both_watched = []
    # for i in range(len(user_data["watched"])):
    #     for j in range(len(user_data["friends"])):
    #         for k in range(len(user_data["friends"][j]["watched"])):
    #             if user_data["watched"][i]["title"] == user_data["friends"][j]["watched"][k]["title"] \
    #                 and user_data["watched"][i]["title"] not in list_both_watched:
    #                 list_both_watched.append(user_data["watched"][i])
    # list_user_watched = []
    # for i in range(len(user_data["watched"])):
    #     list_user_watched.append(user_data["watched"][i])
    # 
    # list_unique_watched = []
    # for item in list_user_watched:
    #     if item not in list_both_watched:
    #         list_unique_watched.append(item)


    list_friend_watched = []
    for i in range(len(user_data["friends"])):
        for j in range(len((user_data)["friends"][i]["watched"])):
            list_friend_watched.append(user_data["friends"][i]["watched"][j])

    list_user_watched = [item for item in user_data["watched"]]

    list_unique_user_watched = []
    for item in list_user_watched:
        if item not in list_friend_watched:
            list_unique_user_watched.append(item)

    return list_unique_user_watched

def get_friends_unique_watched(user_data):
    # Method that doesn't use list comprehension, and would work if a friend gave a move a different rating than the user
    # list_both_watched = []
    # for i in range(len(user_data["watched"])):
    #     for j in range(len(user_data["friends"])):
    #         for k in range(len(user_data["friends"][j]["watched"])):
    #             if user_data["watched"][i]["title"] == user_data["friends"][j]["watched"][k]["title"] \
    #                 and user_data["watched"][i]["title"] not in list_both_watched:
    #                 list_both_watched.append(user_data["watched"][i])
    
    # list_friend_watched = []
    # for j in range(len(user_data["friends"])):
    #         for k in range(len(user_data["friends"][j]["watched"])):
    #             list_friend_watched.append(user_data["friends"][j]["watched"][k])

    # list_unique_friend_watched = []
    # for item in list_friend_watched:
    #     if item not in list_both_watched and item not in list_unique_friend_watched:
    #         list_unique_friend_watched.append(item)

    list_friend_watched = []
    for i in range(len(user_data["friends"])):
        for j in range(len((user_data)["friends"][i]["watched"])):
            list_friend_watched.append(user_data["friends"][i]["watched"][j])

    list_user_watched = [item for item in user_data["watched"]]

    list_unique_friend_watched = []
    for item in list_friend_watched:
        if item not in list_user_watched and item not in list_unique_friend_watched:
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

def get_new_rec_by_genre(user_data):

    genre_dict = {}
    for movie_dict in user_data["watched"]:
        movie_genre = movie_dict["genre"]
        if movie_genre in genre_dict.keys():
            genre_dict[movie_genre] += 1
        else:
            genre_dict[movie_genre] = 1
    
    most_frequent_genres = []
    for genre_name, popularity in genre_dict.items():
        if popularity == max(genre_dict.values()):
            most_frequent_genres.append(genre_name)
    
    recommended_movies = []
    friend_recs = get_friends_unique_watched(user_data)
    for i in range(len(friend_recs)):
        if friend_recs[i]["genre"] in most_frequent_genres:
            recommended_movies.append(friend_recs[i])
    
    return recommended_movies

def get_rec_from_favorites(user_data):
    no_friends_watched_list = get_unique_watched(user_data)
    recommendations = []
    for item in user_data["favorites"]:
        if item in no_friends_watched_list:
            recommendations.append(item)
    return recommendations
    


