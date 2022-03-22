from collections import Counter

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title":title,
        "genre":genre,
        "rating":rating
    }

    for val in movie_dict.values():
        if not val:
            return None

    return movie_dict

def add_to_watched(user, movie):

    for key in user:
        user[key].append(movie)
    
    return user

def add_to_watchlist(user, movie):

    for key in user:
        user[key].append(movie)
    
    return user

def watch_movie(user_data, movie):
    
    filtered_user_data = dict(user_data)

    for elem in user_data["watchlist"]:
        watched_movie = elem["title"]
        if movie == watched_movie:
            filtered_user_data["watched"].append(elem)
            filtered_user_data["watchlist"].remove(elem)

    return filtered_user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    tot_rating = 0.0
    
    if not user_data["watched"]:
        return tot_rating

    for elem in user_data["watched"]:
        tot_rating += elem["rating"]
    
    return tot_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_list = []

    if not user_data["watched"]:
        return None

    for elem in user_data["watched"]:
        genre_list.append(elem["genre"])
        
    counters = Counter(genre_list)
    return max(counters, key=counters.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    friend_movies = []
    my_movies = []
    if not user_data["watched"]:
        return my_movies

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie["title"])
    friend_movies = set(friend_movies)
    
    for my_watched in user_data["watched"]:
        if my_watched["title"] not in friend_movies:
            my_movies.append(my_watched)

    return my_movies

def get_friends_unique_watched(user_data):

    friend_movies = []
    my_movies = []

    for my_watched in user_data["watched"]:
        my_movies.append(my_watched["title"])
    my_movies = set(my_movies)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_movies: #remove duplicates from friend_movies
                if movie["title"] not in my_movies:
                    friend_movies.append(movie)
    
    return friend_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------