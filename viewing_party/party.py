
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}

    if title == None or genre == None or rating == None:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)

    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            add_to_watched(user_data, title)

    return user_data
        
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    
    # make a list with the movies rating
    rating_list = []
    for movie in watched_movies:
       rating_list.append(movie["rating"])

    # count average rating
    if len(rating_list) == 0:
        avg_rating = 0
    else:
        avg_rating = sum(rating_list)/len(rating_list)

    return avg_rating

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    genre_list = []

    # make a list of genres
    for movie in watched_movies:
       genre_list.append(movie["genre"])

    # check that genre list is not empty
    if len(genre_list) == 0:
        return None
    
    # my solution assume that it will be just one most watched genre, no possibility for two or more
    pop_genre = genre_list[0]
    counter = 1
    most_watched_genre_dict = {}
    for genre in genre_list:
        if genre not in most_watched_genre_dict:
            most_watched_genre_dict[genre] = 1
        else: 
            most_watched_genre_dict[genre] += 1
            if most_watched_genre_dict[genre] > counter:
                pop_genre = genre
                counter = most_watched_genre_dict[genre]
            
    return pop_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# additional function to get the list of friends watched dictionaries
def get_friends_watched_list(user_data):
    friends = user_data["friends"]
    friends_watched_list = []
    for friend in friends:
        for film in friend["watched"]:
            friends_watched_list.append(film)
    return friends_watched_list

def get_unique_watched(user_data):
    watched_movies = user_data["watched"]

    # get the list of friends watched dictionaries
    friends_watched_list = get_friends_watched_list(user_data)
    
    # get unique just by user watched movies
    just_user_watched = []
    for movie in watched_movies:
        if movie not in friends_watched_list:
            just_user_watched.append(movie)
    return just_user_watched

def get_friends_unique_watched(user_data):   
    watched_movies = user_data["watched"]

    # get the list of friends watched dictionaries
    friends_watched_list = get_friends_watched_list(user_data)
    
    # get unique just by friends watched movies
    just_friend_watched = []
    for friend_movie in friends_watched_list:
        if friend_movie not in watched_movies:
            if friend_movie not in just_friend_watched:
                just_friend_watched.append(friend_movie)
    return just_friend_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    # collect data: watched movies, list of subscriptions, friends watch list
    watched_movies = user_data["watched"]
    user_subscriptions= user_data["subscriptions"]
    friends_watched_list = get_friends_watched_list(user_data)
   
    # make a recomendation list by subscription
    recomendation_list = []
    for friend_movie in friends_watched_list:
        if friend_movie not in watched_movies:
            if friend_movie["host"] in user_subscriptions:
                recomendation_list.append(friend_movie)
    return recomendation_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # find user's most frequently watched genre, collect data: watched movies, friends watch list
    watched_movies = user_data["watched"]
    user_most_watched_genre = get_most_watched_genre(user_data)
    friends_watched_list = get_friends_watched_list(user_data)
    
    # check for data not to be empty
    recommended_movies = []
    if len(watched_movies) == 0 or len(friends_watched_list) == 0:
        return recommended_movies
    else:
    # make a recomendation list by genre
        for friend_movie in friends_watched_list:
            if friend_movie not in watched_movies:
                if friend_movie["genre"] in user_most_watched_genre:
                    recommended_movies.append(friend_movie)
        return recommended_movies

def get_rec_from_favorites(user_data):
    # get favorites from user_data and collect other data: watched movies, friends watch list
    favorite_user_movies = user_data["favorites"]
    friends_watched_list = get_friends_watched_list(user_data)
    watched_movies = user_data["watched"]

    # check for data not to be empty
    recommended_movies_for_friends = []
    if len(watched_movies) == 0 or len(friends_watched_list) == 0:
        return recommended_movies_for_friends
    # create list of favorite movies recomendation
    else:
        for movie in watched_movies:
            if movie in favorite_user_movies:
                if movie not in friends_watched_list:
                    recommended_movies_for_friends.append(movie)
        return recommended_movies_for_friends