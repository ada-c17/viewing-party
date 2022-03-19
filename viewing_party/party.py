# ------------- WAVE 1 --------------------

from re import U

# Creates a dictionary for a movie if the parameters are all truthy
def create_movie(title, genre, rating):
    if all([title, genre, rating]):
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None

# Add movie to the user's watched list of movies
def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)
    return user_data

# Add movie to the user's watchlist list of movies
def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

# Move a movie from the user's watchlist to watched list 
def watch_movie(user_data, title):
    index = 0
    transfer_movie = False
    watched_list = user_data["watched"]
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            transfer_movie = watchlist.pop(index)
            break
        index += 1
    if transfer_movie:
        watched_list.append(transfer_movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Calculates the average rating (float) for all watched movies
def get_watched_avg_rating(user_data):
    ratings = []
    movie_list = user_data["watched"]
    
    for dict in movie_list:
        ratings.append(dict["rating"])
    
    if not ratings:
        return 0.0
    else:
        return sum(ratings) / float(len(ratings))

# Find the most watched genre in watched list
def get_most_watched_genre(user_data):
    genre_list = []
    watched_list = user_data["watched"]
    
    for movie in watched_list:
        genre_list.append(movie["genre"])
    
    max_genre = max(genre_list, default=None, key=genre_list.count)
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Return list of movie dicts that only the user has watched
def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]

    # Each index is a "friend" holding a dictionary
    friends_list = user_data["friends"]
    # List will hold movie dicts on one level
    friends_watched_list = []
    for friend in friends_list:
        friends_watched_list += friend["watched"]
    # m is movie dict
    unique_list = [m for m in user_watched_list if m not in friends_watched_list]
    return unique_list

# Return list of movie dicts that only friends have watched
def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    unique_list = []

    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in user_watched_list and movie not in unique_list:
                unique_list.append(movie)
    return unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# Return list of movie recommendations based on user's subscriptions
def get_available_recs(user_data):
    subscription_list = user_data["subscriptions"]
    friends_watched_list = get_friends_unique_watched(user_data)
    # m is movie dict
    rec_list = [m for m in friends_watched_list if m["host"] in subscription_list]
    return rec_list

#user-data
    #key "subscriptions"
        #list of strings

    # key "friends" (value is a list)
        #index is dictionary for each friend
            #key - 'watched' is list
                #each index is a movie's dictionary
                    #key "host", for subscribtion service
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Return list of movie recommendations based on favorite genre
def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    friends_watched_list = get_friends_unique_watched(user_data)
    # m is movie dict
    rec_list = [m for m in friends_watched_list if m["genre"] == fav_genre]
    return rec_list

# Return list of movie dicts that is a user favorite and friends haven't watched
def get_rec_from_favorites(user_data):
    # user_data has key "favorites", which is a list of dictionaries
    user_favs = user_data["favorites"]
    friends_watched_list = user_data["friends"]
    movie_recs = []
    
    for user_movie in user_favs:
        watched_movie = False
        for friend in friends_watched_list:
            for friend_movie in friend["watched"]:
                if user_movie == friend_movie:
                    watched_movie = True
        if not watched_movie:
            movie_recs.append(user_movie)
    return movie_recs
