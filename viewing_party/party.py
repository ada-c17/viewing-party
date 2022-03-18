# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    for value in movie_dict.values():
        if value == None:
            return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            add_to_watched(user_data, movie)
            del user_data["watchlist"][i]
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    average_rating = 0
    for i in range(len(user_data["watched"])):
        ratings.append(user_data["watched"][i]['rating'])
    if len(ratings) > 0:
        average_rating = sum(ratings)/len(ratings)
    else:
        average_rating = sum(ratings)
    return average_rating

def get_most_watched_genre(user_data):
    genres = []
    for i in range(len(user_data["watched"])):
        genres.append(user_data["watched"][i]['genre'])
    if len(genres) == 0:
        return None
    else:
        popular_genre = max(set(genres), key = genres.count)
    return popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_movies = []
    friend_movies = []
    unique_user_movies = []
    # generate user movies list
    for i in range(len(user_data["watched"])):
        user_movies.append(user_data["watched"][i])
    # generate friend watched movies list
    for dict in user_data["friends"]:
        for key, value in dict.items():
            if key == "watched":
                for i in value:
                    friend_movies.append(i)
    # find users unique movies
    for i in user_movies:
        if i not in friend_movies and i not in unique_user_movies:
            unique_user_movies.append(i)
    return unique_user_movies

def get_friends_unique_watched(user_data):
    user_movies = []
    friend_movies = []
    unique_friend_movies = []
    # generate user movies list
    for i in range(len(user_data["watched"])):
        user_movies.append(user_data["watched"][i])
    # generate friend watched movies list
    # get friends data dictionaries
    for dict in user_data["friends"]:
        # get each friends' watched dictionary
        for key, value in dict.items():
            # if the key of the dict is watched, then add that key's value to the movie list
            if key == "watched":
                for i in value:
                    friend_movies.append(i)
    # find users unique movies
    for i in friend_movies:
        if i not in user_movies and i not in unique_friend_movies:
            unique_friend_movies.append(i)
    return unique_friend_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_friend_movies = get_friends_unique_watched(user_data)
    user_subscriptions = user_data['subscriptions']
    recommendations = []

    for movie in unique_friend_movies:
        for key, value in movie.items():
            if key == "host" and value in user_subscriptions:
                recommendations.append(movie)
    
    return recommendations



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

